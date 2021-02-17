def method1(int1):
    list1 = list(str(int1))
    a = 0
    for i in list1:
        a += int(i) ** 2
    return a

c = 2
cnt = 0
list89 = [89]
list01 = [1]
while c < 10000000:
    b = c

    while method1(b) != 1 and method1(b) != 89:
        b = method1(b)
        if b in list89:
            print(c, 89)
            list89.append(c)
            cnt += 1
            break
        if b in list01:
            list01.append(c)
            break
    if method1(b) == 89:
        list89.append(c)
        print(c,method1(b))
        cnt += 1
    if method1(b) == 1:
        list01.append(c)
    c += 1

print(cnt)