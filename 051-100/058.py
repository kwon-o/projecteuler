import math

def sosu(i):
    z = 1
    if type(i) != int or i<2:
        z = 0
    for j in range(2, int(i ** 0.5) + 1 ):
        if i % j == 0:
            z = 0
    return z


su = 1
sosu1 = 1.0
zensu1 = 1.0
j = 0

while ((sosu1)/zensu1) > 0.1:
    j += 2
    roop = 0
    while roop < 4:
        su += j
        zensu1 += 1.0

        if sosu(su) == 1:
            sosu1 += 1.0
        roop += 1

    print((sosu1-1.0)/zensu1, math.sqrt(su))
