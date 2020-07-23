def transitionPoint(arr, n):
    #Code here
    if sum(arr)==0:
        return -1
    elif sum(arr) ==n:
        return 0
    else:
        return search(arr,0,n-1)

def search(arr,l,r):
    if r>=l:
        mid = l+(r-l)//2
        if (arr[mid],arr[mid+1])==(0,1):
            return mid+1
        elif arr[mid]==1:
            return search(arr,l,mid-1)
        else:
            return search(arr,mid+1,r)

arr=[0,0,0,0,0,0,0,0,0,0,0,0,1,1]
n = len(arr)
print(transitionPoint(arr,n))