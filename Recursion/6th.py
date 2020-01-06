# Fibonnaci sequence

def fib(n):
	x=0
	y=1
	i=0
	while x<=n:
		print x
		x,y=y,x+y
		i+=1
	

fib(input('Enter a number: ')) 
