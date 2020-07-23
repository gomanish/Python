# Who has the majority

def majorityWins(A,n,x,y):
    count_x = 0
    count_y = 0
    for i in range(n):
        if A[i]==x:
            count_x+=1
        elif A[i]==y:
            count_y+=1
    if count_x == count_y:
        return min(x,y)
    elif (count_x>count_y):
        return x
    elif(count_y>count_x):
        return y


T = int(input())
while(T>0):
    n=int(input())
    arr = [int(x) for x in input().split()]
    x,y = map(int,input().split())
    print(majorityWins(arr,n,x,y))
    T-=1
