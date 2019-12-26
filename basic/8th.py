''' MAKES TWENTY: Given two integers, returns true if the sum of 
the integers is 20 or if one of the integer is 20. if not return
False'''

def makes_twenty(n1,n2):
	return(n1==20 or n2==20 or n1+n2==20)

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))
