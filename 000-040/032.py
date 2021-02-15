result = 0
c1 = []
for a in range(1,10000):
    for b in range(1,10000):
        pan = []
        c = a * b

        lstA = list(str(a))
        lstB = list(str(b))
        lstC = list(str(c))

        for i in lstA:
            if (i not in pan) and (i != '0'):
                pan.append(i)
            else:
                pan.append('x')
        for i in lstB:
            if (i not in pan) and (i != '0'):
                pan.append(i)
            else:
                pan.append('x')
        for i in lstC:
            if (i not in pan) and (i != '0'):
                pan.append(i)
            else:
                pan.append('x')

        if len(pan) == 9 and 'x' not in pan and c not in c1:
            c1.append(c)
            print(a, b, c, pan)
            result += c
            print(result)
