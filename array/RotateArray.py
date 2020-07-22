def rotateArr(A,N,D):
    L = 0
    R= D-1
    while(L<R):
        A[L],A[R] = A[R],A[L]
        L +=1
        R -=1
    L = D
    R= N-1
    while(L<R):
        A[L],A[R] = A[R],A[L]
        L +=1
        R -=1
    A.reverse()
    return



T = int(input())
while(T>0):
    nd = [int(x) for x in input().split()]
    N = nd[0]
    D = nd[1]
    A = [int(x) for x in input().split()]
    rotateArr(A,N,D)
    print(*A)
    T -=1