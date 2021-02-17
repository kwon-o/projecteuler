r = 1
for i in range(1,101):
    r *= i

lst = list(str(r))
sum = 0
for i in lst:
    sum += int(i)

print(sum)