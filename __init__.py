bl_info = {
    "name": "Frontier's Cobra Engine Formats (JWE, Planet Zoo)",
    "author": "Harlequinz Ego, HENDRIX et al.",
    "blender": (3, 2, 0),
    "version": (3, 0, 2),
    "location": "File > Import-Export",
    "description": "Import-Export models, skeletons and animations",
    "warning": "",
    "wiki_url": "https://github.com/OpenNaja/cobra-tools",
    "support": 'COMMUNITY',
    "tracker_url": "https://github.com/OpenNaja/cobra-tools/issues/new",
    "category": "Import-Export"}

try:
    import os
    import sys
    import subprocess
    import logging
    import pkg_resources, importlib.util

    import bpy
    import bpy.utils.previews
    from bpy.props import IntProperty
    from bpy.types import PropertyGroup
    import addon_utils

    copies_of_tools = []
    for addon in addon_utils.modules():
        if addon.bl_info['name'] == bl_info['name']:
            copies_of_tools.append(addon)
    if len(copies_of_tools) > 1:
        addon_paths = "\n".join(os.path.dirname(addon.__file__) for addon in copies_of_tools)
        raise UserWarning(f"You have multiple copies of the tools installed in your blender addons folders:\n"
                          f"{addon_paths}\nClose blender, delete all but the current version and try again.")

    plugin_dir = os.path.dirname(__file__)
    if not plugin_dir in sys.path:
        sys.path.append(plugin_dir)

    from ovl_util.logs import logging_setup
    logging_setup("blender_plugin")
    logging.info(f"Running blender {'.'.join([str(x) for x in bpy.app.version])}")
    from root_path import root_dir

    from plugin import addon_updater_ops
    from plugin.addon_updater_ops import classes as updater_classes
    from plugin.modules_import.operators import ImportBanis, ImportManis, ImportMatcol, ImportFgm, ImportMS2, ImportSPL, \
        ImportVoxelskirt, ImportMS2FromBrowser, ImportFGMFromBrowser
    from plugin.modules_export.operators import ExportMS2, ExportSPL, ExportManis, ExportBanis, ExportFgm
    from plugin.utils.operators import UpdateFins, UpdateLods, VcolToComb, CombToVcol, TransferHairCombing, AddHair, \
    GenerateRigEdit, ApplyPoseAll, ConvertScaleToLoc, ExtrudeFins, IntrudeFins, Mdl2Rename, Mdl2Duplicate, \
    AutosmoothAll, LODS_UL_items
    from plugin.utils.properties import CobraSceneSettings, CobraMeshSettings, CobraCollisionSettings, \
    CobraMaterialSettings, LodData
    from plugin.utils.panels import CobraMaterialPanel, CobraMdl2Panel, VIEW_PT_Mdl2

    global preview_collection


    class CobraPreferences(bpy.types.AddonPreferences):
        """Cobra preferences"""
        bl_idname = __package__

        # Addon updater preferences.
        auto_check_update: bpy.props.BoolProperty(
            name="Auto-check for Update",
            description="If enabled, auto-check for updates using an interval",
            default=False)

        updater_interval_months: bpy.props.IntProperty(
            name='Months',
            description="Number of months between checking for updates",
            default=0,
            min=0)

        updater_interval_days: bpy.props.IntProperty(
            name='Days',
            description="Number of days between checking for updates",
            default=1,
            min=0,
            max=31)

        updater_interval_hours: bpy.props.IntProperty(
            name='Hours',
            description="Number of hours between checking for updates",
            default=0,
            min=0,
            max=23)

        updater_interval_minutes: bpy.props.IntProperty(
            name='Minutes',
            description="Number of minutes between checking for updates",
            default=0,
            min=0,
            max=59)

        def draw(self, context):
            # we are only suggesting to install bitarray for now
            bitarray_spec = importlib.util.find_spec("bitarray")
            if bitarray_spec is None:
                row = self.layout.row()
                row.alert = True
                button = row.operator("wm.install_dependencies",
                         text="Some modules are not installed (click to install)",
                         icon="ERROR")

            addon_updater_ops.update_settings_ui(self, context)


    class InstallDependencies(bpy.types.Operator):
        """Installs: bitarray-hardbyte"""
        bl_idname = "wm.install_dependencies"
        bl_label = "Install missing dependencies, requires restarting"
        bl_options = {'REGISTER'}

        def execute(self, context):
            # from the suggested modules list, remove those installed already
            # pkg_resources might not look into the addon-packages folder
            missing = {'bitarray-hardbyte'} - {pkg.key for pkg in pkg_resources.working_set}
            python = sys.executable
            # can't write in site-packages, but we can write in the addon-packages folder
            subprocess.call([python, '-m', 'pip', 'install', *missing, '-t', os.path.join( bpy.utils.user_resource("SCRIPTS"), 'addons', 'modules')], stdout=subprocess.DEVNULL)
            return {'FINISHED'}


    class MESH_PT_CobraTools(bpy.types.Panel):
        """Creates a Panel in the scene context of the properties editor"""
        bl_label = "Cobra Mesh Tools"
        bl_space_type = 'PROPERTIES'
        bl_region_type = 'WINDOW'
        bl_context = "data"

        @classmethod
        def poll(cls, context):
            if context.active_object.type == 'MESH':
                return True
            else:
                return False

        def draw(self, context):
            addon_updater_ops.check_for_update_background()
            addon_updater_ops.update_notice_box_ui(self, context)
            
            layout = self.layout
            row = layout.row(align=True)
            row.operator("object.add_hair", icon="CURVES")

            box = layout.box()
            box.label(text="Combing", icon="CURVES")
            sub = box.row(align=True)
            sub.operator("object.vcol_to_comb", icon="COPYDOWN")
            sub.operator("object.comb_to_vcol", icon="PASTEDOWN")
            box.operator("object.transfer_hair_combing", icon="PASTEFLIPDOWN")

            box = layout.box()
            box.label(text="Fur Fins", icon="SEQ_HISTOGRAM")
            box.operator("object.update_fins", icon="FILE_REFRESH")
            row = box.row(align=True)
            row.operator("object.extrude_fins", icon="ADD")
            row.operator("object.intrude_fins", icon="REMOVE")


    class SCENE_PT_CobraTools(bpy.types.Panel):
        """Creates a Panel in the scene context of the properties editor"""
        bl_label = "Cobra Scene Tools"
        bl_space_type = 'PROPERTIES'
        bl_region_type = 'WINDOW'
        bl_context = "scene"

        @classmethod
        def poll(cls, context):
            return True

        def draw(self, context):
            layout = self.layout
            row = layout.row(align=True)
            row.prop(context.scene.cobra, "num_streams")
            row = layout.row(align=True)
            row.prop(context.scene.cobra, "game")
            addon_updater_ops.update_notice_box_ui(self, context)


    class COLLISION_PT_CobraTools(bpy.types.Panel):
        """Creates a Panel in the scene context of the properties editor"""
        bl_label = "Cobra Collision Tools"
        bl_space_type = 'PROPERTIES'
        bl_region_type = 'WINDOW'
        bl_context = "physics"

        @classmethod
        def poll(cls, context):
            if context.active_object.rigid_body:
                return True
            return False

        def draw(self, context):
            rb = context.active_object.cobra_coll
            layout = self.layout
            row = layout.row(align=True)
            row.prop(rb, "air_resistance")
            row = layout.row(align=True)
            row.prop(rb, "damping_3d")
            row = layout.row(align=True)
            row.prop(rb, "flag")
            row = layout.row(align=True)
            row.prop(rb, rb.get_current_versioned_name(context, "surface"))
            row = layout.row(align=True)
            row.prop(rb, rb.get_current_versioned_name(context, "classification"))


    def draw_rigid_body_constraints_cobra(self, context):
        scene = context.scene
        layout = self.layout

        # display properties and values
        col = layout.column(align=True)
        # col.label(text="My Values:")
        col.prop(context.active_object.cobra_coll, "plasticity_min")
        col.prop(context.active_object.cobra_coll, "plasticity_max")
        # col.prop(scene, "plasticity", text="Frame Start")


    def menu_func_export(self, context):
        icon = preview_collection["frontier.png"].icon_id
        self.layout.operator(ExportFgm.bl_idname, text="Cobra Material (.fgm)", icon_value=icon)
        self.layout.operator(ExportMS2.bl_idname, text="Cobra Model (.ms2)", icon_value=icon)
        self.layout.operator(ExportSPL.bl_idname, text="Cobra Spline (.spl)", icon_value=icon)
        self.layout.operator(ExportBanis.bl_idname, text="Cobra Baked Anim (.banis)", icon_value=icon)
        self.layout.operator(ExportManis.bl_idname, text="Cobra Anim (.manis)", icon_value=icon)


    def menu_func_import(self, context):
        icon = preview_collection["frontier.png"].icon_id
        self.layout.operator(ImportFgm.bl_idname, text="Cobra Material (.fgm)", icon_value=icon)
        self.layout.operator(ImportMatcol.bl_idname, text="Cobra Material (.matcol, .dinosaurmateriallayers)",
                             icon_value=icon)
        self.layout.operator(ImportMS2.bl_idname, text="Cobra Model (.ms2)", icon_value=icon)
        self.layout.operator(ImportBanis.bl_idname, text="Cobra Baked Anim (.banis)", icon_value=icon)
        self.layout.operator(ImportManis.bl_idname, text="Cobra Anim (.manis)", icon_value=icon)
        self.layout.operator(ImportSPL.bl_idname, text="Cobra Spline (.spl)", icon_value=icon)
        self.layout.operator(ImportVoxelskirt.bl_idname, text="Cobra Map (.voxelskirt)", icon_value=icon)

    # Function used to inject elements in the contextual menu of the File Browser editor
    def CT_FileBrowser_Context_Menu(self, context):
        if context.space_data.browse_mode == 'FILES' and context.active_file:
            file     = context.active_file.name
            folder   = context.space_data.params.directory.decode('ascii')
            filepath = os.path.join(folder, file)
            fileext  = os.path.splitext(file)[1]

            if os.path.isfile(filepath):
                if fileext.lower() == ".ms2":
                    layout = self.layout
                    layout.separator()
                    layout.operator(ImportMS2FromBrowser.bl_idname)

                if fileext.lower() == ".fgm":
                    layout = self.layout
                    layout.separator()
                    layout.operator(ImportFGMFromBrowser.bl_idname)


    classes = (
        ImportBanis,
        ImportManis,
        ImportMatcol,
        ImportFgm,
        ImportMS2,
        ImportSPL,
        ImportMS2FromBrowser,
        ImportFGMFromBrowser,
        ExportFgm,
        ExportMS2,
        ExportSPL,
        ExportBanis,
        ExportManis,
        ImportVoxelskirt,
        UpdateFins,
        LodData,
        LODS_UL_items,
        UpdateLods,
        GenerateRigEdit,
        ApplyPoseAll,
        ConvertScaleToLoc,
        VcolToComb,
        CombToVcol,
        ExtrudeFins,
        IntrudeFins,
        TransferHairCombing,
        AddHair,
        CobraPreferences,
        CobraSceneSettings,
        CobraMeshSettings,
        CobraCollisionSettings,
        CobraMaterialSettings,
        CobraMaterialPanel,
        CobraMdl2Panel,
        VIEW_PT_Mdl2,
        Mdl2Rename,
        Mdl2Duplicate,
        AutosmoothAll,
        MESH_PT_CobraTools,
        SCENE_PT_CobraTools,
        COLLISION_PT_CobraTools,
        InstallDependencies,
        *updater_classes
    )
except:
    logging.exception("Startup failed")
    pass

# get panel names
# for panel in bpy.types.Panel.__subclasses__():
#     print(panel.__name__)
# PHYSICS_PT_rigid_body
# PHYSICS_PT_rigid_body_settings
# PHYSICS_PT_rigid_body_collisions
# PHYSICS_PT_rigid_body_collisions_surface
# PHYSICS_PT_rigid_body_collisions_sensitivity
# PHYSICS_PT_rigid_body_collisions_collections
# PHYSICS_PT_rigid_body_dynamics
# PHYSICS_PT_rigid_body_dynamics_deactivation
# PHYSICS_PT_rigid_body_constraint
# PHYSICS_PT_rigid_body_constraint_settings
# PHYSICS_PT_rigid_body_constraint_objects
# PHYSICS_PT_rigid_body_constraint_override_iterations
# PHYSICS_PT_rigid_body_constraint_limits
# PHYSICS_PT_rigid_body_constraint_limits_linear
# PHYSICS_PT_rigid_body_constraint_limits_angular
# PHYSICS_PT_rigid_body_constraint_motor
# PHYSICS_PT_rigid_body_constraint_motor_angular
# PHYSICS_PT_rigid_body_constraint_motor_linear
# PHYSICS_PT_rigid_body_constraint_springs
# PHYSICS_PT_rigid_body_constraint_springs_angular
# PHYSICS_PT_rigid_body_constraint_springs_linear
def register():
    addon_updater_ops.register(bl_info)
    icons_dir = os.path.join(root_dir, "icons")
    global preview_collection
    preview_collection = bpy.utils.previews.new()
    for icon_name_ext in os.listdir(icons_dir):
        icon_name = os.path.basename(icon_name_ext)
        preview_collection.load(icon_name, os.path.join(icons_dir, icon_name_ext), 'IMAGE')

    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

    # insert properties
    bpy.types.Material.fgm   = bpy.props.PointerProperty(type=CobraMaterialSettings)
    bpy.types.Scene.cobra = bpy.props.PointerProperty(type=CobraSceneSettings)
    bpy.types.Mesh.cobra = bpy.props.PointerProperty(type=CobraMeshSettings)
    # bpy.types.RigidBodyObject.cobra = bpy.props.PointerProperty(type=CobraCollisionSettings)
    bpy.types.Object.cobra_coll = bpy.props.PointerProperty(type=CobraCollisionSettings)

    # Injection of elements in the contextual menu of the File Browser editor
    bpy.types.FILEBROWSER_MT_context_menu.append(CT_FileBrowser_Context_Menu)
    bpy.types.PHYSICS_PT_rigid_body_constraint_limits_angular.append(draw_rigid_body_constraints_cobra)


def unregister():

    # Injection of elements in the contextual menu of the File Browser editor
    bpy.types.FILEBROWSER_MT_context_menu.remove(CT_FileBrowser_Context_Menu)
    bpy.types.PHYSICS_PT_rigid_body_constraint_limits_angular.remove(draw_rigid_body_constraints_cobra)

    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.cobra
    del bpy.types.Mesh.cobra
    global preview_collection
    bpy.utils.previews.remove(preview_collection)


if __name__ == "__main__":
    register()
