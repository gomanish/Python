# Array Pair Sum

def pair_sum(arr,k):
	out=set()
	temp=set()
	for num in arr:
		diff=k-num
		if diff not in temp:
			temp.add(num)
		else:
			out.add((num,diff))

	print(out)    #output all the unique pairs that sum up to a specific value k.


pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)
