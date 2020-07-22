# find the maximum appearing element
# Soution-1
# O(N*M) time complexity
def maxAppearing(L,R):
    d = {}
    for i,j in zip(L,R):
        for k in range(i,j+1):
            if k not in d.keys():
                d[k] = 1
            else:
                d[k]+=1
    max = 0
    for i in d.keys():
        if d[i]>max:
            max = i
    return max

L = [1,2,5,15]
R = [5,8,7,18]
#print(maxAppearing(L,R))


# Solution-2
# if the value of L[i],R[i] <= 100
def maxOccr(L,R,n):
    arr = [0]*100
    for i in range(n):
        arr[L[i]]+=1
        arr[R[i]+1]-=1
    maxm = arr[0]
    res = 0
    for i in range(1,100):
        arr[i]+=arr[i-1]
        if maxm<arr[i]:
            maxm=arr[i]
            res = i
    return res

n=len(L)
print(maxOccr(L,R,n))

