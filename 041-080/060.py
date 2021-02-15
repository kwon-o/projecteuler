def sosu(i):
    z = 1
    if type(i) != int or i<2:
        z = 0
    for j in range(2, int(i ** 0.5) + 1 ):
        if i % j == 0:
            z = 0
    return z

def find_sosu( thelist ):
    z = 1
    sum_min = 99999999999999999999999
    for i in range(0, len(thelist)-1, 1):
        if z == 0:
            break
        for j in range(i+1, len(thelist), 1):
            str1 = str(thelist[i]) + str(thelist[j])
            str2 = str(thelist[j]) + str(thelist[i])
            if (sosu(int(str1)) + sosu(int(str2))) != 2:
                z = 0
                break
            elif sum_min > int(str1) or sum_min > int(str2):
                sum_min = min( int(str1) , int(str2) )
    if z == 1:
        return sum_min
    else:
        return False

'''print(find_sosu( [ 3, 7, 109, 673 ] ))'''

def mklist():
    sosu_list = []
    for i in range(1,5000,1):
        if sosu(i) == 1:
            sosu_list.append(i)
    return sosu_list

y = False
while y == False:
    find_list = mklist()
    for a in range(1, len(find_list)-4, 1):
        if y != False:
            break
        for b in range(a+2, len(find_list)-3, 1):
            if y != False:
                break
            for c in range(b+25, len(find_list)-2, 1):
                if y != False:
                    break
                for d in range(c+80, len(find_list)-1, 1):
                    if y != False:
                        break
                    for e in range(d+1, len(find_list),1):
                        check_list = [find_list[a], find_list[b], find_list[c], find_list[d], find_list[e]]
                        print(check_list)
                        if find_sosu(check_list) != False:
                            y = find_sosu(check_list)
                            print(find_sosu(check_list))
                            break
