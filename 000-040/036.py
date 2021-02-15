def deaching(a):
    list1 = list(str(a))
    m = int(len(list1) / 2)
    cnt = 0
    for i in range(0,m):
        if list1[i] == list1[len(list1)-1-i]:
            cnt += 1
        if cnt == m:
            return True

def binary(n):
    b_list = []
    q = 0
    r = 0
    b_digit = 0
    result = ''
    while True:
        q = int(n/2)
        r = int(n%2)
        b_digit += 1
        b_list.append((q,r))
        if q != 0:
            n = q
        else: break
    for i in range(len(b_list)):
        result += str(b_list[-(i+1)][1])
    return int(result)

sum = 0
for i in range(1,1000000):
    if deaching(i) == True:
        if deaching(binary(i)) == True:
            sum += i
            print(i, binary(i))

print('sum:', sum)

