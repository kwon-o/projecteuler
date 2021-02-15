for a in range (1, 600):
    for b in range(a+1, 600):
        for c in range(b+1, 600):
            if (a**2 + b**2 == c **2) and (a+b+c == 1000):
                print (a,b,c)
                print (a*b*c)
                break