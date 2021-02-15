cnt_list = []
def res(lst):
    for i in lst:
        if i in cnt_list:
            return False
            break
        else:
            cnt_list.append(i)
    return True



list_17 = []
for i in range(1,1000):
    if i % 17 == 0:
        list_17.append(str(i))

