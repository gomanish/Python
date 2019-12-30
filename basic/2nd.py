'''Write a program that print the integers from 1 to 100. 
But the multiple of three print "Fizz" instead of the number,
and for the multiple of five print "Buzz" .for numbers which 
are multiple of both three and five print "FizzBuzz". '''




for num in range(1,101):
	if num%3==0 and num%5==0:
		print("FizzBuzz")
	elif num%3==0:
		print("Fizz")
	elif num%5==0:
		print("Buzz")
	else:
		print(num)
