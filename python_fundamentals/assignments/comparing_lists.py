def compare_lists(list0, list1):
	if len(list0) != len(list1):
		print "The lists are not the same."
	else:
		for i in range(0, len(list0)):
			if list0[i] != list1[i]:
				print "the lists are not the same."
				return
		print "The lists are the same."


l1_a = [1,2,5,6,2]
l1_b = [1,2,5,6,2]

l2_a = [1,2,5,6,5]
l2_b = [1,2,5,6,5,3]

l3_a = [1,2,5,6,5,16]
l3_b = [1,2,5,6,5]

l4_a = ['celery','carrots','bread','milk']
l4_b = ['celery','carrots','bread','cream']

compare_lists(l1_a, l1_b)
compare_lists(l2_a, l2_b)
compare_lists(l3_a, l3_b)
compare_lists(l4_a, l4_b)

