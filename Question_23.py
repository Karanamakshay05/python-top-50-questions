#Pyramid Sum
#Explaination:
#       1
#    2  1  2
# 3  2  1  2  3
# Sum= 1+5+11=17

# a = int(input())  #Kiran's Code
# b = 1
# lis = [1]
# for i in range(2,a+1):
#     b =b+i*2
#     lis.append(b)
# print(sum(lis))

input_1=int(input())
result=input_1*1
num=2
for i in range(input_1-1,0,-1):
    result+=2*i*num
    num+=1
print(result)