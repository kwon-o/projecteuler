def prod(x, a):
    pro = int(x * a)
    x = sort(pro)
    return x, pro

def sort(x):
    str_x = list(str(x))
    str_x.sort()
    x = ''.join(str_x)
    return x

for i in range(100000, 166666):
    result_list = []
    result_list.append(int(i))
    for j in range(2,7):
        if prod(i,j)[0] == sort(i):
            result_list.append(prod(i,j)[1])

    if len(result_list) == 6:
        print(result_list)
        print(i)