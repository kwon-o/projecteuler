
for i in range(10,100):
    a1 = (list(str(i)))

    for j in range(10,100):
        b1 = (list(str(j)))

        c1 = i/j

        if a1[0] == b1[1]:
            del a1[0]
            del b1[1]
            a2 = int(''.join(a1))
            b2 = int(''.join(b1))
            try:
                c2 = a2/b2
            except ZeroDivisionError:
                pass
            if c1 == c2 and c1 < 1:
                print(i, j)
                a1 = (list(str(i)))
            else:
                a1 = (list(str(i)))
        elif a1[1] == b1[0]:
            del a1[1]
            del b1[0]
            a2 = int(''.join(a1))
            b2 = int(''.join(b1))
            try:
                c2 = a2/b2
            except ZeroDivisionError:
                pass
            if c1 == c2 and c1 < 1:
                print(i, j)
                a1 = (list(str(i)))
            else:
                a1 = (list(str(i)))