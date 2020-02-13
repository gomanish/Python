#  Leaders in an array

arr=[55,3,20,15,8,25,3]
l=len(arr)
max=0
for x in range(0,len(arr)):
	if max<arr[l-1]:
		max=arr[l-1]
		print max,
	
	l=l-1
