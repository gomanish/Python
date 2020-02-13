'''Write a function repfree(s) that takes as input a string s and checks whether any character appears more than once.
The function should return True if there are no repetitions and False otherwise.'''


def repfree(string):
	for x in range(len(string)):
		temp=0
		if string[x] in string[x+1:]:
			return False
	return True
