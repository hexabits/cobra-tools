from generated.formats.guestonrideanimsettings.imports import name_type_map
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class GuestOnRideAnimSettingsRoot(MemStruct):

	__name__ = 'GuestOnRideAnimSettingsRoot'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.unk_0 = name_type_map['Uint64'](self.context, 0, None)
		self.ptr = name_type_map['Pointer'](self.context, 0, name_type_map['GuestOnRideAnimSettingsChild'])
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'ptr', name_type_map['Pointer'], (0, name_type_map['GuestOnRideAnimSettingsChild']), (False, None), (None, None)
		yield 'unk_0', name_type_map['Uint64'], (0, None), (False, None), (None, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'ptr', name_type_map['Pointer'], (0, name_type_map['GuestOnRideAnimSettingsChild']), (False, None)
		yield 'unk_0', name_type_map['Uint64'], (0, None), (False, None)
