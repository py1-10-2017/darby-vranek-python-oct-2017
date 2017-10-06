def multiples():
	for i in range(1, 1000):
		if i % 2 != 0:
			print i


def sum_list(list):
	sum = 0
	for value in list:
		sum += value
	return sum


def average_list(list):
	sum = sum_list(list)
	return sum / len(list)


# multiples()

# print sum_list([1, 2, 5, 10, 255, 3])

# print average_list([1, 2, 5, 10, 255, 3])