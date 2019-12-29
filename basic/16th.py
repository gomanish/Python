''' SPY GAME: Write a function that takes in a list of integers and return 
True if it contain 007 ni order'''

def spy_game(nums):
	a=[0,0,7,'p']

	for num in nums:
		if num==a[0]:
			a.pop(0)

	return len(a)==1

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([[1,7,2,0,4,5,0]]))
