

def fec(int):
    if int == 0:
        return 1
    pro = 1
    for i in range(1,int+1):
        pro *= i
    return pro

result_list = []
for n in range(1, 101):
    for r in range(1, n+1):
        com = fec(n) / (fec(r)*fec(n-r))
        if com > 1000000:
            print(com, n, r)
            result_list.append(com)

print(len(result_list))
