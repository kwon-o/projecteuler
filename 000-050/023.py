def yaksu_sum(number):
    y_sum = 0
    t_num = int(number / 2)

    while t_num >= 1:
        if number % t_num == 0:
            y_sum += t_num
        t_num -= 1

    return y_sum

def sosu(i):
    z = 1
    if type(i) != int or i<2:
        z = 0
    for j in range(2, int(i ** 0.5) + 1 ):
        if i % j == 0:
            z = 0
    return z

a = 2
Non_abundant = []

while a < 14062:
    s = 0
    if sosu(a) == 0:
        if a < yaksu_sum(a):
            Non_abundant.append(a)
            print(a)
    a +=1

print(Non_abundant)

 