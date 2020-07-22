def reverseInGroups(A,N,K):
    #Your code here
    temp = 0
    while(temp<N):
        L = temp
        R= min(temp+K-1,N-1)
        while(L<R):
            A[L],A[R] = A[R],A[L]
            L +=1
            R -=1
        temp +=K
    return

T = int(input())
while(T>0):
    nk = [int(x) for x in input().split()]
    N = nk[0]
    K = nk[1]
    A = [int(x) for x in input().split()]
    reverseInGroups(A,N,K)
    print(*A)
    T-=1
