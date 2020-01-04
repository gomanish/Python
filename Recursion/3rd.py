''' create a function called split which takes in a string phrase set of list of words.
The function will then determine if it is possible to split the string in a way in which
word can be made from the list of words.You can assume the phrase will only contain word 
found in dictionary if it is completely splittable.'''


def word_split(phrase,list_of_word,output=None):
	if output is None:
		output=[]

	for word in list_of_word:
		if phrase.startswith(word):
			output.append(word)

			return word_split(phrase[len(word)::],list_of_word,output)

	output=" ".join(output)
	return output



k='mynameismanishkumar'
l=['manish','name','mayank','my','is','kumar']
print word_split(k,l)

