def pandi(lst):
    a = len(lst)
    pandi_list = []
    for j in range(1,a+1):
        pandi_list.append(str(j))
    if len(lst) != a:
        return False
    else:
        for i in lst:
            try:
                pandi_list.remove(i)
            except ValueError:
                pass
        if pandi_list == []:
            return True
        else:
            return False

def sosu(i):
    z = 1
    if type(i) != int or i<2:
        z = 0
    for j in range(2, int(i ** 0.5) + 1 ):
        if i % j == 0:
            z = 0
    return z


result_list = []
for a in range(10,1000000000):
    b = list(str(a))
    if pandi(b) == True:
        if sosu(a) == 1:
            print(a)
            result_list.append(a)

print(result_list)
