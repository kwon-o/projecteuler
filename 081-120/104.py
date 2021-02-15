f1 = 1
f2 = 1
cnt = 2

finder = '123456789'

while True:
    f3 = f1 + f2
    f3_1 = list(str(f3)[:9])
    f3_1.sort()
    f3_1 = ''.join(f3_1)

    f3_2 = list(str(f3)[-9:])
    f3_2.sort()
    f3_2 = ''.join(f3_2)

    if f3_1 == finder and f3_2 == finder:
        print(f3)
        print(cnt + 1)
        break
    else:
        f1 = f2
        f2 = f3
        cnt += 1
        print(cnt)
