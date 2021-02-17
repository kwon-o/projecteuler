s1 = 1
s2 = 2
result = 0

while s2 < 4000000:
    if s2 % 2 == 0:
        result += s2

    i = s1
    s1 = s2
    s2 = i + s1

print(result)