def sosu(i):
    cnt = 0
    for j in range(2, i):
        if i % j == 0:
            return False
            break
        cnt += 1
        if cnt == i - 2:
            return True

def yaksu(int1):
    yaksu_list=[]
    for i in range(2,int1+1):
        if int1 % i == 0:
            yaksu_list.append(i)

    return yaksu_list



n=2
result = 0
Totient_maximum=0
while n <= 1000000:
    cnt = 1.0
    for i in range(2,n):
        cnt_in = 0
        for m in yaksu(i):
            if m in yaksu(n):
                break
            cnt_in += 1.0
        if cnt_in == len(yaksu(i)):
            cnt += 1.0
    print(float(n), float(cnt), float(n/cnt))
    if Totient_maximum < float(n/cnt):
        result = n
        Totient_maximum = float(n/cnt)
    n += 1
print(result, Totient_maximum)