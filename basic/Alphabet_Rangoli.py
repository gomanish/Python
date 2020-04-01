n=int(input())
al='abcdefghijklmnopqrstuvwxyz'
m1=(4*n)-3
for x in range(1,n+1):
    k=n-1
    for y in range(1,m1+1):
        if (y>(2*n)-(2*x) and y<(2*n-2)+(2*x) and (y%2!=0) ):
            print(al[k],end="")
            if y<int(m1/2)+1:
                k-=1
            else:
                k+=1
        else:
            print('-',end='')
    print()

for x in range(n-1,0,-1):
    k=n-1
    for y in range(1,m1+1):
        if (y>(2*n)-(2*x) and y<(2*n-2)+(2*x) and (y%2!=0) ):
            print(al[k],end="")
            if y<int(m1/2)+1:
                k-=1
            else:
                k+=1
        else:
            print('-',end='')
    print()
