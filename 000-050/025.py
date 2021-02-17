F = []
F.append(1)
F.append(1)

for i in range(2,10000):
    if len(list(str(F[i-2] + F[i-1]))) < 1000:
        F.append(F[i-2] + F[i-1])
        print(i+1, F[i-2] + F[i-1])