def sosu(i):
    z = 1
    if type(i) != int or i<2:
        z = 0
    for j in range(2, int(i ** 0.5) + 1 ):
        if i % j == 0:
            z = 0
    return z

a = 11
list_result = []
while len(list_result) < 11:
    a += 2
    t = str(a)
    for i in range(1, len(t)+1):
        if ( sosu(int(t[:i])) + sosu(int(t[-i:])) ) != 2:
            break
        elif i==len(t) and sosu(a)==1:
            list_result.append(a)
            print(a)

print(sum(list_result), list_result)