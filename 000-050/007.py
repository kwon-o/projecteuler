pri = []
pri.append(2)
for i in range(2,1000000):
    cnt = 0
    for j in range (2,i):
        if i % j == 0:
            break
        cnt +=1
        while len(pri) < 10002:
            if cnt == i-2:
                print(i)
                pri.append(i)
            break

print(len(pri))
print(pri[10000])