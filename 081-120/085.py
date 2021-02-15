import math

def combi(int1, int2):
    result = 1
    for i in range(0,int2):
        result *= int1-i
    result = result / math.factorial(int2)

    return result

min1 = 99999999
for i in range(10,100):
    for j in range(10, 100):
        result = combi(i,2) * combi(j,2)
        if result > 1900000 and result < 2100000:
            if abs(result - 2000000) < min1:
                min1 = abs(result - 2000000)
                print(min1, result, i-1, j-1, (i-1)*(j-1))