''' Write a recursive function which takes an integer and 
computes the cumulative sum of 0 to that integer '''

def rec_sum(num):
	if num ==0:
		return num

	return num+rec_sum(num-1)


print rec_sum(10)
