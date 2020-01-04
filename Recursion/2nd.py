''' Given an integer, creat a function which returns the sum of all the 
individual digits in that integer. '''


def sum_func(num):
	if num/10==0:
		return num
	return (num%10)+(sum_func(num/10))


print sum_func(987654321)
