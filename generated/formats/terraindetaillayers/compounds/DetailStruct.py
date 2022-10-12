from generated.formats.base.basic import Float
from generated.formats.base.basic import Uint
from generated.formats.ovl_base.compounds.MemStruct import MemStruct


class DetailStruct(MemStruct):

	__name__ = 'DetailStruct'

	_import_key = 'terraindetaillayers.compounds.DetailStruct'

	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)
		self.index = 0
		self.x = 0.0
		self.y = 0.0
		self.z = 0.0
		if set_default:
			self.set_defaults()

	_attribute_list = MemStruct._attribute_list + [
		('index', Uint, (0, None), (False, None), None),
		('x', Float, (0, None), (False, None), None),
		('y', Float, (0, None), (False, None), None),
		('z', Float, (0, None), (False, None), None),
		]

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'index', Uint, (0, None), (False, None)
		yield 'x', Float, (0, None), (False, None)
		yield 'y', Float, (0, None), (False, None)
		yield 'z', Float, (0, None), (False, None)