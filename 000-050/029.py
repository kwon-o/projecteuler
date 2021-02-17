result = []
for a in range(2,101):
    for b in range(2,101):
        c = a**b
        if c not in result:
            result.append(c)
print(len(result))