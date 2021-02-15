def sosu(i):
    z = 1
    if type(i) != int or i<2:
        z = 0
    for j in range(2, int(i ** 0.5) + 1 ):
        if i % j == 0:
            z = 0
    return z

def yaksu(number):
    divisors = []
    t_num = int(number / 2)

    divisors.append(number)
    while t_num >= 1:
        if number % t_num == 0:
            divisors.append(t_num)
        t_num -= 1
    divisors.sort()
    return divisors

a = 2
amicable = {}

while a < 10000:
    s = 0
    if sosu(a) == 0:
        for i in range(0, len(yaksu(a))-1):
            s += yaksu(a)[i]
        amicable[a] = s
    a +=1

print(amicable)

ami_sum = 0
for i in amicable.items():
    for j in amicable.items():
        if i[0] == j[1] and i[1] == j[0] and i[0] != i[1]:
            print(i[0], i[1])
            ami_sum += i[0]
print ami_sum