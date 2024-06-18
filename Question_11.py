# The function accepts two integers n, m as arguments Find the sum of all numbers
# in range from 1 to m(both inclusive) that are not divisible by n. Return difference 
# between sum of integers not divisible by n with sum of numbers divisible by n.

# Assumption:

# n>0 and m>0
# Sum lies between integral range
# Example

# Input
# n:4
# m:20
# Output
# 90
def checksum(n,m):
    for i in range(1,n+1):
        if(i%m!=0):
            not_divisible_sum+=1

            return original_sum-not_divisible_sum

n=int(input())
m=int(input())
original_sum=n*(n+1)/2
not_divisible_sum=0
print(checksum(n,m,original_sum))

