''' Linear Search
The Linear search function returns the location of k
in given array if present otherwise -1
'''

def LinearSearch(arr,k):
    for i in range(len(arr)):
        if(arr[i]==k):
            return i
    return -1

t = int(input("How many testcases: "))
while(t>0):
    arr = [int(x) for x in input().split()]
    k = int(input("Enter the number that want to search: "))
    i = LinearSearch(arr,k)
    if(i>0):
        print(f"{k} is at index {i} in given array")
    else:
        print("number not found")
