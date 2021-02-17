import math
def sosu(i):
    z = 1
    if type(i) != int or i<2:
        z = 0
    for j in range(2, int(i ** 0.5) + 1 ):
        if i % j == 0:
            z = 0
    return z

sosu_list = []
for i in range(7073):
    if sosu(i) == 1:
        sosu_list.append(i)

cnt = []
for i in sosu_list:
    if i ** 4 > 50000000:
        break
    for j in sosu_list:
        if j ** 3 > 50000000:
            break
        for k in sosu_list:
            tri = i**4 + j**3 + k**2
            if k**2 > 50000000:
                break
            if tri < 50000000:
                cnt.append(tri)
            else:
                print('break', tri, k, j, i)
                break
print(len(list(set(cnt))))