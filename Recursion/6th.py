# Fibonnaci sequence (up to given number n)

def fib(n):
	x=1
	y=1
	for i in range(n):
		print x
		x,y=y,x+y

num=input('Enter a number: ')
fib(num) 


#Using Recursion (print only nth number)
def fib_rec(n):
	if n==0 or n==1:
		return n
	else:
		return fib_rec(n-1) + fib_rec(n-2)

print '\n'
print fib_rec(num)

