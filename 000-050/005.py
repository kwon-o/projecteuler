
for i in range(10,9999999):
    cnt = 0
    for j in range (1,21):
        if i % j == 0:
            cnt += 1
            if cnt == 20:
                print(i)
                break