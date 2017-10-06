def type_list(list):
	string = ""
	sum = 0
	for value in list:
		if isinstance(value, int) or isinstance(value, float):
			sum += value
		elif isinstance(value, str)





type_list(['magical unicorns',19,'hello',98.98,'world'])