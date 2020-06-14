# Flipping an image

def fliping(x):
    # x is a matrix
    for row in range(len(x)):
        for element in range(len(x[row])):
            if x[row][element]==0:
                x[row][element]=1
            else:
                x[row][element]=0
        x[row]=x[row][::-1]
    return(x)


a = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(fliping(a))
b = [[1,1,0],[1,0,1],[0,0,0]]
print(fliping(b))
