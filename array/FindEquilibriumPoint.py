# Find Equilibrium Point 

def EquilibriumPoint(arr,n):
    
    # Find Total sum
    Totalsum = sum(arr)
    # Take left sum initially
    l_sum = 0
    
    for i in range(n):
        # check every point if it is equilibrium point or not
        if l_sum==Totalsum-arr[i]:
            return True
        l_sum +=arr[i]
        Totalsum -=arr[i]
    return False
        
arr = [3,4,8,-9,20,6]
l = len(arr)

if EquilibriumPoint(arr,l):
    print('YES')
else:
    print('NO')
