# Find Laegest Continuous sum in given array

def largest_cont_sum(arr):
	sum=0
	temp=0
	for n in arr:
		sum = max(sum+n , n)
		temp=max(sum,temp)
	return temp


arr1=[1,2,-1,3,4,-1]
print(largest_cont_sum( arr1))
