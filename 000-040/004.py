result1 = ''
for i in range (100,1000):
    for j in range (100,1000):
        s = i * j
        result = []
        for x in range(5,-1,-1):
            k = int(s / 10 ** x)
            result.append(k)
            s = s - k * 10**x


        cnt = 0
        for o,p in enumerate(result):
            if o < (len(result)-1)/2:
                if p == result[len(result)-1-o]:
                    cnt += 1;
        if cnt == 3:
            print(result)
