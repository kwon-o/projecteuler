def sosu(i):
    z = 1
    if type(i) != int or i<2:
        z = 0
    for j in range(2, int(i ** 0.5) + 1 ):
        if i % j == 0:
            z = 0
    return z

sosu_list = []
for i in range(1,1000000):
    if sosu(i) == 1:
        sosu_list.append(i)
print(sosu_list)

result_list = []
result_sum = 0
b_max = 0
for i, num in enumerate(sosu_list):
    a = i
    sum = num
    while a < len(sosu_list)-1 and sum <= 1000000:
        a += 1
        sum += sosu_list[a]
        if sum in sosu_list:
            b = a-i+1
            if b_max < b:
                b_max = b
                result_sum = sum
                print(b_max, result_sum)
            result_list.append((b, sum))

print(b_max, result_sum)