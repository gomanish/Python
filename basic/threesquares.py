'''Write a Python function threesquares(m) that takes an integer m as input and returns True.
if m can be expressed as the sum of three squares and False otherwise.
(If m is not positive, your function should return False.)'''

def threesquares(n):
	if n<0:
		return False
	
	while(n%4==0):
		n=n/4

	n=n-7
	if(n%8==0):
		return False
	return True
