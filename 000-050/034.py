def fect(int):
    result = 1
    for i in range(1,int+1):
        result *= i
    return result

result = 0
for i in range(3,100000):
    list1 = list(str(i))
    sum = 0
    for j in list1:
        sum += fect(int(j))

    if sum == i:
        print(sum)
        result += i

print(result)