# Rotation of array and reversing an array

arr=input("Enter an array : ")
d=int(input("How many times you want to rotate an array : "))

def rotate_an_array(arr,d):
	return(arr[d:len(arr)]+arr[0:d])


def reverse(arr):
	return(arr[::-1])


print("After {} rotation array is : {}" .format(d,rotate_an_array(arr,d)))
print("After reversing array is :  {}".format(reverse(arr)))
