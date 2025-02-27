# 1) Signature for LCM
# Given two numbers a and b. Find the GCD and LCM of and d.
# Input:
# •⁠  ⁠Two positive integers a and b (1 <=a, b <=1000)
# Output:
# For GCD function, an integer representing the GCD of a 'and b
# For LCM function, an integer representing the LCM of a and b
# Sample Input:
# 12 18
# Output:
# 6
# 36

#gcd with Euclidian algorithm
#lcm finding
# a=int(input())
# b=int(input())

# def GCD(a,b):
#     while(b>0):
#         a=b
#         b=a%b
#     return a
# print(GCD(a,b))

# def LCM(a,b):
#     return (a*b)//GCD(a,b)
# print(LCM(a,b))

#GCD with Euclidian algorithm
#LCM finding
def Gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
def Lcm(a,b):
    return (a*b)//Gcd(a,b)
a=int(input())
b=int(input())
print(Gcd(a,b))
print(Lcm(a,b))