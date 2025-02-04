texchannels = {
	'pAOTexture': {"": "AO"},
	'pAlphaTexture': {"": "OP"},
	'pBaseAOTexture': {"R": "AO", "G": "BA"},  # BC5
	'pBaseColourTexture': {"RGB": "BC", "A": "CA"},  # check if A is used here  # Metallic_Roughness_Clip A = OP
	# 'pBaseColourTextureDetailBase': {"RGB": "", "A": ""},
	# 'pBaseColourTextureDetailBlend': {"RGB": "", "A": ""},
	# 'pBaseDielectricSpecularLevelTexture': {"": ""},
	'pBaseDiffuseTexture': {"": "BC"},
	'pBaseNormalTexture': {"RG": "NM", "B": "SP", "A": "RN"},
	# 'pCavityRoughnessDielectricArray': {"R": "", "G": "", "B": "", "A": ""},
	# 'pDetailNormalTexture': {"": ""},
	# 'pDetailRoughnessTexture': {"": ""},
	'pDiffuseAlphaTexture': {"RGB": "BC", "A": "OP"},
	# 'pDiffuseArray': {"": ""},
	'pDiffuseTexture': {"": "BC"},
	'pDinosaurFeathers_BaseDiffuseTexture': {"": "BC"},
	'pEmissiveTexture': {"": "EM"},
	# 'pEnvironmentalNoiseMask': {"": ""},
	'pFeathersBaseDiffuseTexture': {"": "BC"},
	'pFeathers_AOHeightOpacityTransmission_PackedTexture': {"R": "AO", "G": "HE", "B": "OP", "A": "TR"},
	# 'pFeathers_Aniso_PackedTexture': {"R": "", "G": "", },
	'pFeathers_BaseColourTexture': {"": "DE"},
	'pFeathers_EmissiveTexture': {"": "EM"},
	'pFeathers_NormalTexture': {"RG": "NM"},
	'pFeathers_RoughnessPackedTexture': {"R": "MT", "G": "RN", "B": "SP", "A": ""},  # unsure about A
	'pFinAlphaTexture': {"R": "OP", "G": "OP", "B": "OP", "A": "OP"},
	'pFlexiColourMasksTexture': {"R": "F1", "G": "F2", "B": "F3", "A": "F4"},
	# 'pFoamMapTexture': {"": ""},
	# 'pFoamyAreasDistantMap': {"": ""},
	# 'pFullScaleDiffuseAndSpecial': {"": ""},
	# 'pGradHeightArray': {"RG": "", "B": "", "A": ""},
	# 'pHeightTexture': {"": ""},
	# 'pHyperloops_AlphaEmissiveMaskTexture': {"": ""},
	# 'pHyperloops_DiffuseTexture': {"": ""},
	'pIridescenceMaskTexture': {"": "IM"},  # used on UV1 for feathers
	'pIridescenceTexture': {"": "IR"},  # a LUT for reflection coordinates
	# 'pLayered_BlendWeights': {"R": "", "G": "", "B": "", "A": ""},
	# 'pLayered_DiffuseTexture': {"R": "", "G": "", "B": "", "A": ""},
	# 'pLayered_HeightTexture': {"R": "", "G": "", "B": "", "A": ""},
	# 'pLayered_PackedTexture': {"R": "", "G": "", "B": "", "A": ""},
	# 'pLayered_RemapTexture': {"R": "", "G": "", "B": "", "A": ""},
	# 'pLayered_WarpOffset': {"": ""},
	# 'pMacroDiffuse': {"": ""},
	# 'pModelViewer_GridPatternMap': {"": ""},
	# 'pMoiseNoiseMask': {"": ""},
	# 'pMossBaseColour': {"": ""},
	# 'pMossBaseColourRoughnessPackedTexture': {"RGB": "", "A": ""},
	# 'pMossNormalTexture': {"": ""},
	# 'pMossVarianceTexture': {"": ""},
	# 'pNormalBlendWeightTexture': {"": ""},
	# 'pNormalMapTextureUnique': {"": ""},
	'pNormalTexture': {"RGB": "NM", "A": "AO"},  # BC7_UNORM - no coord dropping? not sure if A is actually always AO
	# 'pNormalTextureDetailBase': {"RGB": "", "A": ""},
	# 'pNormalTextureDetailBlend': {"RGB": "", "A": ""},
	'pOpacityTexture': {"": "OP"},
	# 'pPOM_DisplacementRelaxedConeTexture': {"": ""},
	# 'pPackedTexture': {"RGB": "", "A": ""},
	# 'pPatchBlendMap': {"": ""},
	# 'pPatterning_FeathersPatchworkGradientMap': {"": ""},
	# 'pPatterning_FeathersPatternGradientMap': {"": ""},
	# 'pPatterning_PatchworkGradientMap': {"": ""},
	# 'pPatterning_PatternGradientMap': {"": ""},
	# 'pPrimaryBlendMap': {"": ""},
	# 'pProjection_BackgroundPlaneDiffuseTexture': {"": ""},
	# 'pProjection_BackgroundPlaneEmissiveTexture': {"": ""},
	# 'pProjection_DiffuseTexture': {"": ""},
	# 'pProjection_EmissiveTexture': {"": ""},
	# 'pProjection_ForegroundPlaneDiffuseTexture': {"": ""},
	# 'pProjection_ForegroundPlaneEmissiveTexture': {"": ""},
	# 'pProjection_Plane0Texture': {"": ""},
	# 'pProjection_Plane1Texture': {"": ""},
	# 'pProjection_Plane2Texture': {"": ""},
	# 'pProjection_Texture': {"": ""},
	# 'pRemapTexture': {"": ""},
	'pRoughnessPackedTexture': {"R": "MT", "G": "SP", "B": "RN", "A": "FO"},  # Metallic_Roughness_Clip_Geometry_Decal A = OP
	# 'pRoughnessTexture': {"": ""},
	# 'pShellMap': {"R": "", "G": "", "B": "", "A": ""},
	# 'pSpecularTexture': {"": ""},
	# 'pSubLayerDiffuse0Texture': {"": ""},
	# 'pSubLayerDiffuse1Texture': {"": ""},
	# 'pThicknessTexture': {"": ""},
	# 'pWaterBottomHeight': {"": ""},
	# 'pWaterDetailGradientMap': {"": ""},
	# 'pWaterDetailHeightMap': {"": ""},
	# 'pWaterDetailNormalMapTexture': {"": ""},
	# 'pWaterDetailSpecMapTexture': {"": ""},
	# 'pWaterNormalMapTexture': {"": ""},
	# 'pWaterRipplesTexture': {"": ""},
	# 'pWaterRoughnessMapTexture': {"": ""},
	# 'u_basePatchworkMap': {"": ""},
	# 'u_basePatternMap': {"": ""},
	# 'u_feathersBasePatchworkMap': {"": ""},
	# 'u_feathersBasePatternMap': {"": ""},
}
