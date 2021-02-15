str1 = '0'
a = 0
while len(str1) < 1000001:
    a += 1
    b = str(a)
    str1 = str1 + b
result_list = list(str1)

result = 1
for i in range(0,7):
    sq = 10**i
    result *= int(result_list[sq])


print(result)