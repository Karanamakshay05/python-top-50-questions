# The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array 
# ‘arr’ of size ‘n’ as its argument ‘r’ represents the number of rats present in an area, 
# ‘unit’ is the amount of food each rat consumes and each ith element of array ‘arr’ represents
# the amount of food present in ‘i+1’ house number, where 0 <= i

# Note:

# Return -1 if the array is null
# Return 0 if the total amount of food from all houses is not sufficient for all the rats.
# Computed values lie within the integer range.
# Example:

# Input:

# r: 7
# unit: 2
# n: 8
# arr: 2 8 3 5 7 4 1 2
# Output:

# 4
def rat(r,unit):
    food=0
    count=0
    req=r*unit
    n=int(input())
    arr=list(map(int,input().split()))
    if arr==[]:
        return -1
    for i in range(0,n):
        if req>0:
            req=arr[i]
            count+=1
    if(count==n):
        return "food not sufficient"
    else:
        return count
r=int(input("no. of rats"))
unit=int(input("Food for each rat"))
print(rat(r,unit))