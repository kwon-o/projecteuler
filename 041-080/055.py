def deaching(int1):
    str_lst = list(str(int1))
    lst = []
    for i in str_lst:
        lst.append(int(i))
    cnt = 0
    for i in range(0,int(len(lst)/2)+1):
        if lst[i] == lst[len(lst)-1-i]:
            cnt += 1
        else:
            return False
            break
        if cnt == int(len(lst)/2) + 1:
            return True

def rever(int1):
    str_lst = list(str(int1))
    str_lst.reverse()
    rever_num = int(''.join(str_lst))
    return rever_num


Lychrel_numbers = []
for i in range(10, 10001):
    a = i
    roop = 0
    while deaching(a + rever(a)) == True or roop < 50:
        if deaching(a + rever(a)) == True:
            break
        else:
            a = a + rever(a)
            roop += 1
        if roop == 50:
            Lychrel_numbers.append(i)

print(Lychrel_numbers)
print(len(Lychrel_numbers))