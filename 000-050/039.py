result_list = []
for a in range(1,1000):
    for b in range(1,a+1):
        c = a ** 2 + b ** 2
        if int(c ** 0.5) == c ** 0.5:
            if len(str(a + b + int(c ** 0.5))) < 4 or (a + b + int(c ** 0.5)) == 1000:
                result_list.append(a + b + int(c ** 0.5))

print(result_list)

max_cnt = 0
max_val = 0
for i in range(1,1000):
    cnt = result_list.count(i)
    if max_cnt < cnt:
        max_cnt = cnt
        max_val = i

print(max_cnt, max_val)