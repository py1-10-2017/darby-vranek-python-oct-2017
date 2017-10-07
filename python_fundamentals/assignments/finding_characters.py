def find_characters(word_list, char):
	output = list()
	for word in word_list:
		if char in word:
			output.append(word)
	return output



print find_characters(['hello','world','my','name','is','Anna'], "o")