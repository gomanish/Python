''' BLACKJACK: Given three integers between 1 and 11, if their sum is less
than or equal to 21, return their sum. If their sum exceeds 21 and there's 
an eleven, reduce the total sum by 10. Finally, if the sum (even after 
adjustment) exceeds 21, return 'BUST' '''

def blackjack(a,b,c):
	num=a+b+c
	if num<=21:
		return num
	elif 11 in [a,b,c] and num<=31:
		return num-10
	else:
		 return 'BUST'


print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))
