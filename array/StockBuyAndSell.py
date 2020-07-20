# Stock Buy And Sell


# Function to find all the local maxima 
# and minima in the given array arr[] 
def findLocalMaximaMinima(n,arr):
    # empty list to store point of 
    # local maxima and minima
    mx = []
    mn = []
    # Checking whether the first point is local maxima or minima
    # or neither
    if arr[0]>arr[1]:
        mx.append(arr[0])
    elif arr[0]<arr[1]:
        mn.append(arr[0])
    # Iterate over all points to check
    # local maxima and minima

    for i in range(1,n-1):
        # condition for local minima
        if(arr[i-1]>arr[i] and arr[i]<arr[i+1]):
            mn.append(arr[i])
        # condition for local maxima
        elif(arr[i-1]<arr[i] and arr[i]>arr[i+1]):
            mx.append(arr[i])
    
    # Cheacking whether the last point is local maxima or minima

    if arr[-1]>arr[-2]:
        mx.append(arr[-1])
    elif arr[-1]<arr[-2]:
        mn.append(arr[-1])
    
    return mn,mx

def stockbuyandsell(arr):
    # Finding length of tha array
    n = len(arr)
    arr1 = sorted(arr)
    # Cheacking if list element is in decreasing order 
    # then return profit is zero
    if arr==arr1[::-1]:
        return 0
    
    # Function Call To find the array 
    # of all local minima and local maxima
    mn,mx = findLocalMaximaMinima(n,arr)
    result = 0
    for i in range(min(len(mn),len(mx))):
        result+=(mx[i]-mn[i])
    return result

# Given array arr[] 
arr = [1,5,3,8,12] 
print("Maximum Profit is : ",stockbuyandsell(arr))
