class Patient(object):
	def __init__(self, id, name, allergies):
		self.id = id
		self.name = name
		self.allergies = allergies
		self.bed_number = None


class Hospital(object):
	def __init__(self, name, capacity):
		self.name = name
		self.capacity = capacity
		self.patients = list()
		self.beds = [i for i in range(1, self.capacity + 1)]


	def admit(self, patient):
		if len(self.patients) >= self.capacity:
			return 'The hospital is full!'
		else:
			patient.bed_number = self.beds[0]
			self.beds.pop(0)
			self.patients.append(patient)
			return '%s has been assigned bed #%s' % (patient.name, patient.bed_number)

	def discharge(self, patient):
		if patient in self.patients:
			self.beds.append(patient.bed_number)
			patient.bed_number = None
			self.patients.remove(patient)
			return '%s has been discharged.' % patient.name



hospital = Hospital('Happy Bird Hospital', 170)
patients = [Patient(1, 'Aderyn', None), Patient(2, 'Lydia', None), Patient(3, 'Ginger', None)]

for patient in patients:
	print hospital.admit(patient)

for patient in patients:
	print hospital.discharge(patient)


for patient in patients:
	print hospital.admit(patient)
