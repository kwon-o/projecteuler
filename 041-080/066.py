import math

def issquare(n):
    temp = n ** 0.5
    if int(temp) == temp:
        if temp ** 2 == n:
            return True
    return False

square_list = []
for i in range(1,500000):
    square_list.append(i*i)

x_max = 0
for D in range(1,1001):
    if D not in square_list:
        x=2
        while True:
            if issquare(float((x*x - 1) / float(D))) == True:
                print('x',x, 'D', D, 'y', math.sqrt((x*x -1) / D))
                if x_max < x:
                    x_max = x
                break
            x += 1
print(x_max)
