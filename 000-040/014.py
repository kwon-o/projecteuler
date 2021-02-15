
result = []
for m in range(2,1000001):
    cnt = 1
    n = m
    while n != 1:
        if n % 2 == 0:
            n = n/2
            cnt += 1
        else:
            n = (3 * n) + 1
            cnt += 1
    if cnt == 525:
        result.append([cnt, m])
    print(cnt, m)
print(result)

# non