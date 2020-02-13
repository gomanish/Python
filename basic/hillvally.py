'''A list of numbers is said to be a hill if it consists of an ascending sequence followed by a descending sequence, where each of
the sequences is of length at least two. Similarly, a list of numbers is said to be a valley hill if it consists of an descending 
sequence followed by an ascending sequence. You can assume that consecutive numbers in the input sequence are always
different from each other.
Write a Python function hillvalley(l) that takes a list l of integers and returns True if it is a hill or a valley, and False otherwise. '''



def hillvalley(l):
	b=0
	for x in range(1,len(l)-1):
		if ((l[x-1]<l[x]) != (l[x]<l[x+1])):
			b=b+1
	if 0<b<=1:
		return True
	else:
		return False
