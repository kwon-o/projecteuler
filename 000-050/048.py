sum = 0
for i in range(1,1001):
    a = i ** i
    sum += a
print(str(sum)[-10:])