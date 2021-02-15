def yaksu(number):
    divisors = []
    t_num = int(number / 2)

    divisors.append(number)
    while t_num >= 1:
        if number % t_num == 0:
            divisors.append(t_num)
        t_num -= 1
    divisors.sort()
    return divisors

def diopan(n):
    cnt = 0
    for i in range(n+1,n*2+1):
        j = i
        while True:
            if (float(i * j) / float(i + j)) == n:
                print (i,j,(float(i * j) / float(i + j)))
                cnt += 1
                break
            elif (i*j) / (i+j) < n:
                j += 1
            else:
                break
    return cnt

n = 100
while len(yaksu(n))<666:
    print ((len(yaksu(n))))
    n += 1