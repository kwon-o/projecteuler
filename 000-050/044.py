def Pentagonal_list():
    pentagonal_list = []
    for i in range(1,5000):
        pentagonal_list.append(  (i * (3 * i - 1 )) / 2)
    return  pentagonal_list

pen = Pentagonal_list()

min_sub = 999999
for a in pen:
    for b in pen:
        sum1 = a + b
        sub1 = abs(b - a)
        if sum1 in pen and sub1 in pen:
            print(a,b)
            if min_sub > sub1:
                min_sub = sub1

print(min_sub)