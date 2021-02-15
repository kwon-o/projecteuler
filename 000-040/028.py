sum = 1
a = 1
for i in range(3,1002,2):
    for j in range(1,5):
        a += i-1
        sum += a
print(sum)