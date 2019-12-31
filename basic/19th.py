# Find the missing element

def finder(arr1,arr2):
    temp=0
    for num in arr1:
        temp+=num

    for num in arr2:
        temp-=num

    return temp

arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
missing_num=finder(arr1,arr2)
print('{} is the missing number' .format(missing_num))
  
