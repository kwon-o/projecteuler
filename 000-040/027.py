def sosu(i):
    cnt = 0

    for j in range(2, i):
        if i % j == 0:
            return False
            break
        cnt += 1
        if cnt == i - 2:
            return True

max = 0
a1 = 0
b1 = 0
n1 = 0
for a in range(-1000,1001):
    for b in range(-1000,1001):
        cnt = 0
        print(a,b)
        for n in range(0,500):
            if sosu(n**2 + a*n + b) is True:
                cnt += 1
            else:
                break

        if max < cnt:

            max = cnt

            a1 = a
            b1 = b
            n1 = n

print('a=', a1, 'b=', b1, 'n=' , n1, 'a*b=', a1*b1)
