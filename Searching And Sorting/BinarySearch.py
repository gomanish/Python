# Binary Search
# Recursive function
# binarysearch function return the location of the x
# if it present in arr ptherwise return -1
def binarysearch(arr,l,r,x):
    if(r>=l):
        mid = l+(r-l) //2
        # if the element is present at the middle itself
        if(arr[mid]==x):
            return mid
        # if the element is smaller then middle
        if(arr[mid]>x):
            return binarysearch(arr,l,r-1,x)
        # if element is grater then the middle
        if(arr[mid]<x):
            return binarysearch(arr,mid+1,r,x)
    # when element not present in the array
    return -1

# Iterative solution
def BinarySearch(arr,l,r,x):
    while(r>=l):
        mid = l+(r-l)//2
        if (arr[mid]==x):
            return mid
        if(arr[mid]>x):
            r = mid-1
        if(arr[mid]<x):
            l=mid+1
    return -1


arr = [1,22,44,55,77,88,90,91,95,97,99]
x = 99
print(binarysearch(arr,0,len(arr),x))
print(BinarySearch(arr,0,len(arr),x))



