def bbsort(list1):
    for i, num in enumerate(list1):
        if i < len(list1) - 1:
            if num > list1[i + 1]:
                k = num
                list1[i] = list1[i+1]
                list1[i+1] = k
    for i, num in enumerate(list1):
        if i < len(list1) - 1:
            if num > list1[i + 1]:
                bbsort(list1)
    return list1
from collections import Counter as cc


permutations = []
for i in range(100, 10000):
    permutations.append(i*i*i)

sort_permutations = []
for i in permutations:
    sort_permutations.append(''.join(bbsort(list(str(i)))))

print(permutations)
print(sort_permutations)

cnt = cc(sort_permutations)
print(cnt.most_common()[:5])

list012334566789 = []
list012334556789 = []
for i in range(100, 10000):
    if ''.join(bbsort(list(str(i*i*i)))) == '012334566789':
        list012334566789.append(i*i*i)
    elif ''.join(bbsort(list(str(i*i*i)))) == '012334556789':
        list012334556789.append(i*i*i)

print(min(list012334566789))
print(min(list012334556789))