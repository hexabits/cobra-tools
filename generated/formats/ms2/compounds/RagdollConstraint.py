from generated.formats.ms2.compounds.Constraint import Constraint
from generated.formats.ms2.imports import name_type_map


class RagdollConstraint(Constraint):

	__name__ = 'RagdollConstraint'


	def __init__(self, context, arg=0, template=None, set_default=True):
		super().__init__(context, arg, template, set_default=False)

		# the location of the child joint
		self.loc = name_type_map['Vector3'](self.context, 0, None)

		# normed, matches first row of rot
		self.vec_a = name_type_map['Vector3'](self.context, 0, None)

		# all 3 rows are orthogonal to one another
		self.rot = name_type_map['Matrix33'](self.context, 0, None)

		# normed, and orthogonal to vec_a
		self.vec_b = name_type_map['Vector3'](self.context, 0, None)

		# radians
		self.x = name_type_map['RotationRange'](self.context, 0, None)

		# radians
		self.y = name_type_map['RotationRange'](self.context, 0, None)

		# radians
		self.z = name_type_map['RotationRange'](self.context, 0, None)

		# radians
		self.plasticity = name_type_map['RotationRange'](self.context, 0, None)
		if set_default:
			self.set_defaults()

	@classmethod
	def _get_attribute_list(cls):
		yield from super()._get_attribute_list()
		yield 'loc', name_type_map['Vector3'], (0, None), (False, None), (None, None)
		yield 'vec_a', name_type_map['Vector3'], (0, None), (False, None), (None, None)
		yield 'rot', name_type_map['Matrix33'], (0, None), (False, None), (None, None)
		yield 'vec_b', name_type_map['Vector3'], (0, None), (False, None), (None, None)
		yield 'x', name_type_map['RotationRange'], (0, None), (False, None), (None, None)
		yield 'y', name_type_map['RotationRange'], (0, None), (False, None), (None, None)
		yield 'z', name_type_map['RotationRange'], (0, None), (False, None), (None, None)
		yield 'plasticity', name_type_map['RotationRange'], (0, None), (False, None), (None, None)

	@classmethod
	def _get_filtered_attribute_list(cls, instance, include_abstract=True):
		yield from super()._get_filtered_attribute_list(instance, include_abstract)
		yield 'loc', name_type_map['Vector3'], (0, None), (False, None)
		yield 'vec_a', name_type_map['Vector3'], (0, None), (False, None)
		yield 'rot', name_type_map['Matrix33'], (0, None), (False, None)
		yield 'vec_b', name_type_map['Vector3'], (0, None), (False, None)
		yield 'x', name_type_map['RotationRange'], (0, None), (False, None)
		yield 'y', name_type_map['RotationRange'], (0, None), (False, None)
		yield 'z', name_type_map['RotationRange'], (0, None), (False, None)
		yield 'plasticity', name_type_map['RotationRange'], (0, None), (False, None)
