def pandi(lst):
    pandi_list = list(str(123456789))
    if len(lst) != 9:
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

result_pandi = []

for i in range(1,10000):
    str1 = ''
    j = 0
    while len(str1)<9:
        j += 1
        str1 = str1 + str(i*j)
    if pandi(list(str1)) == True:
        print(i)
        print(str1)
        result_pandi.append(str1)

print(max(result_pandi),result_pandi)


