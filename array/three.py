# Trapping rain water


arr=input("Enter an array : ")

leftmax=[]
max2=arr[-1]
for i in range(1,len(arr)+1):
	if max2<arr[-i]:
		max2=arr[-i]
	leftmax.append(max2)

leftmax=leftmax[::-1]

result=0
max1=arr[0]
for i in range(len(arr)):
	if max1<arr[i]:
		max1=arr[i]
	
	m=min(leftmax[i],max1)
	result=result+(m-arr[i])

print result
