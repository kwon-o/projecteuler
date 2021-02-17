import math

num = 9
max_num = 1000000
jari = 0
num_list = [0,1,2,3,4,5,6,7,8,9]
result = []

while num >= 0:
    while max_num > math.factorial(num):
        max_num -= math.factorial(num)
        jari += 1
        print(max_num)
    result.append(num_list[jari])
    del num_list[jari]
    jari = 0
    num -= 1

print(result)