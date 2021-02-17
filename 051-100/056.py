def jarisu_sum(int1):
    list_int = list(str(int1))
    jarisu_result = 0
    for i in list_int:
        jarisu_result += int(i)
    return jarisu_result

max_sum = 0
for a in range(1,100):
    for b in range(1,100):
        if max_sum < jarisu_sum(a ** b):
            max_sum = jarisu_sum(a ** b)

print(max_sum)