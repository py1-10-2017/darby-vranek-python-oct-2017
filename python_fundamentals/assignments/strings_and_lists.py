def find_and_replace(words):
	print words.find("day")
	return words.replace("day", "month")


def min_and_max(values):
	lowest = values[0]
	highest = values[0]
	for value in values:
		if value < lowest:
			lowest = value
		elif value > highest:
			highest = value
	print "min val:", lowest
	print "max val:", highest


def first_and_last(values):
	print "first:", values[0]
	print "last:", values[len(values) - 1]
	return [values[0], values[len(values) -1]]


def new_list(values):
	values.sort()
	half = int(len(values) / 2)
	first = values[:half]
	last = values[half:]
	last.insert(0, first)
	return last


print find_and_replace("It's thanksgiving day. It's my birthday,too!")

min_and_max([2,54,-2,7,12,98])

print first_and_last(["hello",2,54,-2,7,12,98,"world"])

print new_list([19,2,54,-2,7,12,98,32,10,-3,6])

