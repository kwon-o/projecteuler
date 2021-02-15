i = 2
while i < 100000:
    s = 0
    for j in range(1,i):
        s += j
    i += 1

    s2 = s ** 0.5

    if s2 == int(s2):
        cnt = 1
    else:
        cnt = 0
    k = 1
    while k < s2:
        if s % k == 0 :
            cnt += 2
        k += 1
    print(i, s, cnt)
    if cnt >= 500:
        print(i, s, cnt)
        break
