def sosu(i):
    cnt = 0
    for j in range(2, i):
        if i % j == 0:
            return False
            break
        cnt += 1
        if cnt == i - 2:
            return True

def bbsort(list1):
    for i , num in enumerate(list1):
        if i < len(list1) - 2:
            if num > list1[i + 1]:
                k = num
                list1[i] = list1[i+1]
                list1[i+1] = k
    for i, num in enumerate(list1):
        if i < len(list1) - 2:
            if num > list1[i + 1]:
                bbsort(list1)
    return list1

def listka(list1):
    r = []
    for i in list1:
        l1 = list(str(i))
        r.append(bbsort(l1))
    return r

for i in range(1000,3340):
    l = []
    l.append(i)
    l.append(i + 3330)
    l.append(i + 6660)

    if sosu(l[0]) == True and sosu(l[1]) == True and sosu(l[2]) == True:
        if listka(l)[0] == listka(l)[1] == listka(l)[2]:
            print(l)
