class Patient(object):
	"""docstring for Patient."""
	def __init__(self, id, name, allergies):
		self.id = id
		self.name = name
		self.allergies = allergies
		self.bed_number = None


class Hospital(object):
	"""docstring for Hospital."""
	def __init__(self, name, capacity):
		self.name = name
		self.capacity = capacity
		self.patients = list()


	def admit(self, patient):
		if len(self.patients) >= self.capacity:
			return 'The hospital is full!'
