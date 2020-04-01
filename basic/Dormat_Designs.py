n=int(input())
for x in range(int(n/2)):
    for y in range(n):
        if (y>=int(n/2)-x and y<=int(n/2)+x):
            print('.|.',end='')
        else:
            print('---',end='')
    print()
for y in range(3*n-6):
    if (y>int((3*n)/2)-4 and y<int((3*n)/2)-2):
        print('WELCOME',end='')
    else:
        print('-',end='')
print()
for x in range(int(n/2)-1,-1,-1):
    for y in range(n):
        if (y>=int(n/2)-x and y<=int(n/2)+x):
            print('.|.',end='')
        else:
            print('---',end='')
    print()
