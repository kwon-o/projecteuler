'''1 = sosu'''
def sosu(i):
    z = 1
    if type(i) != int or i<2:
        z = 0
    for j in range(2, int(i ** 0.5) + 1 ):
        if i % j == 0:
            z = 0
    return z

def soinsu(int):
    soinsu_list = []
    i = 2
    while int != 1:
        if int % i == 0:
            soinsu_list.append(i)
            int = int / i
            i = 1
        elif sosu(int) == 1:
            soinsu_list.append(int)
            int = int / int
        i += 1
    return soinsu_list

def squ(list1):
    list2 = []
    while list1 != []:
        for i in list1:
            if list1.count(i) > 1:
                list2.append(i ** list1.count(i))
                del list1[0:list1.count(i)]
            else:
                list2.append(i)
                list1.remove(i)
    return list2

banbok = 4

for i in range(100000, 1000000):
    primes = []
    a = 0
    k = i
    find = 0
    if sosu(i) == 0:
        while a < banbok:
            if sosu(k) == 1 or len(squ(soinsu(k))) != banbok:
                primes.append('x')
                break
            else:
                for j in squ(soinsu(k)):
                    primes.append(j)
                k +=1
                a +=1
    print(primes)

    if primes == []:
        continue

    cnt = 0
    for z in primes:
        if primes.count(z) > 1:
            break
        elif primes.count(z) and 'x' not in primes:
            cnt += 1
    if cnt == len(primes):
        find = i
        print('find :', find)
        for x in range(0,banbok):
            print(squ(soinsu(i+x)))
        break
    if find != 0:
        break


