# Program to remove Duplicate element

# This function return new size of modified array
def removeDuplicates(arr,n):
    if n==0 or n==1:
        return n
    # To store store index of next unique element
    j = 0
    for i in range(n-1):
        if arr[i]!=arr[i+1]:
            arr[j]=arr[i]
            j+=1
    arr[j] = arr[n-1]
    j +=1
    return j

arr = [1,2,2,3,4,4,4,5,5]
n = len(arr)
n = removeDuplicates(arr,n)

for i in range(n):
    print(arr[i],end=" ")
