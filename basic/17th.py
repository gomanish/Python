''' COUNT PRIME: Write a function that returns the number of prime 
numbers that exist up to and including a given number'''

def count_primes(num):
	if num<2:
		return 0

	prime=[2]
	x=3
	while x<=num:
		for y in prime:
			if x%y==0:
				x +=2
				break
		else:
			prime.append(x)
			x =x+2
	print(prime)
	return len(prime)

print(count_primes(100))

'''The else block just after for is executed only 
when the loop is NOT terminated by a break statement.'''
