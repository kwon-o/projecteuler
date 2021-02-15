result = []
for i in range(4100,200000):
    print(i)
    lst = list(str(i))
    sum = 0
    for j in lst:
        sum += int(j) ** 5
    if sum == i:
        result.append(i)

print(result)

# [4150, 4151, 54748, 92727, 93084, 194979]

sum = 0
for i in result:
    sum += i
print (sum)