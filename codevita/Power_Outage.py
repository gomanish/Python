# Power Outage Problem

def run(striker,non_striker,n):
    if n%2==0:
        return striker+n,non_striker
    else:
        return non_striker,striker+n

RR1 = float(input())
striker,non_striker = list(map(int, input().split()))
D = input().split()
RR2 = float(input())
r = 0
for i in D:
    if i=='W':
        continue
    else:
        r += int(i)


b = len(D)

B1 = int(((RR2*b)-(6*r))/(RR1-RR2))
R1 = int((RR1*B1)/6)

current_ball = B1%6 + 1

for i in D:
    if i=='W':
        striker = 0
    else:
        striker,non_striker = run(striker,non_striker,int(i))
    current_ball +=1

    if current_ball > 6:
        current_ball = 1
        (striker,non_striker) = (non_striker,striker)


totalrun = R1+r
print(totalrun,striker,non_striker)
