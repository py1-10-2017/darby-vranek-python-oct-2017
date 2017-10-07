def type_list(list):
	string = ""
	sum = 0
	hasNum = False
	for value in list:
		if isinstance(value, int) or isinstance(value, float):
			sum += value
			hasNum = True
		elif isinstance(value, str):
			string += " " + value
	if hasNum and len(string) > 0:
		print "The list you entered is of mixed type"
		print "String:" + string
		print "Sum:", sum
	elif len(string) > 0:
		print "The list you entered is of string type"
		print "String: " + string
	else:
		print "The list you entered is of integer type."
		print "Sum:", sum




type_list(['magical unicorns',19,'hello',98.98,'world'])
type_list([2,3,1,7,4,12])
type_list(['magical','unicorns'])