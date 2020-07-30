# Ternary Search

# Recursive Solution
def ternarySearch1(arr ,l,r,k):
    if r >=l:
        mid1 = l + (r-l)//3
        mid2 = r - (r-l)//3
        if arr[mid1]==k:
            return mid1
        if arr[mid2]==k:
            return mid2
        if k<arr[mid1]:
            return ternarySearch1(arr,l,mid1-1,k)
        if k>arr[mid2]:
            return ternarySearch1(arr,mid2+1,r,k)
        else:
            return ternarySearch1(arr,mid1+1,mid2-1,k)
    return "Number Not found"



# Iterative Soution
def ternarySearch2(arr ,l,r,k):
    while(r >= l):
        mid1 = l + (r-l)//2
        mid2 = r - (r-l)//2
        if(arr[mid1] == k):
            return mid1
        if (arr[mid2] == k):
            return mid2
        if(k<arr[mid1]):
            r = mid1-1
            continue
        if k>arr[mid2]:
            l = mid2+1
            continue
        else:
            l = mid1+1
            r = mid2-1
    return "Number Not Found"


# Driver Code
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,44,77,90]
k = 99
print(f"Answer from Recursive Solution: {ternarySearch1(arr,0,len(arr)-1,k)}")
print(f"Answer From iterative Solution: {ternarySearch2(arr,0,len(arr)-1,k)}")