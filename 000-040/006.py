sum1 = 0
for i in range(1,101):
    sum1 += i **2
print(sum1)

sum2 = 0
for i in range(1,101):
    sum2 += i
sum2 = sum2 ** 2

print(sum2 - sum1)