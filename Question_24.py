# Reduce till zero
# Dev loves the number zero. Dev gives Andrew two integers X and Y and asks him to
# perform the steps below on X and Y. until the value of Y has been reduced to zero.
# The below steps should be followed sequentially:
# 2.⁠ ⁠If Y=0. then return X
# 3.⁠ ⁠Otherwise, let T =X-Y.
# 4.⁠ ⁠Set X=Y and then set Y=T
# 5.⁠ ⁠Repeat from step 1.
# Your task is to help Andrew find and return an integer value, representing the value of
# X, when the value of Y has been reduced to zero.
# Note: At least one of the X or Y will be a non-zero integer
# Input Specification:
# input1: An integer value X. representing the first number.
# Input2: An integer value Y, representing the second number
# Sample input: 48
# 18
# Sample Output:
# 6

def solve(X,Y):
    while Y!=0:
        T=X-Y
        X=Y
        Y=T
    return X
X=int(input())
Y=int(input())
print(solve(X,Y))   
 
    


