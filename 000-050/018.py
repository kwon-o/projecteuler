import re
import copy
tri = '''
75 
95 64 
17 47 82 
18 35 87 10 
20 04 82 47 65 
19 01 23 75 03 34 
88 02 77 73 07 63 67 
99 65 04 28 06 16 70 92 
41 41 26 56 83 40 80 70 33 
41 48 72 33 47 32 37 16 94 29 
53 71 44 65 25 43 91 52 97 51 14 
70 11 33 28 77 73 17 78 39 68 17 57 
91 71 52 38 17 14 91 43 58 50 27 29 48 
63 66 04 68 89 53 67 30 73 16 69 87 40 31 
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23 
'''

p = re.compile('\w+(?!\n)')
k = p.findall(tri)
print(len(k))

i = 0
j = 1
tree = []

for n in range (2,17):
    re1 = []
    for m in range(i,j):
        re1.append(int(k[m]))
    i = j
    j += n
    tree.append(re1)

print(tree)

tree_result = copy.deepcopy(tree)

for a in range(1,len(tree)):
    for b in range(0,len(tree[a])):
        if j == 0:
            result_a = 0
        else:
            result_a = tree_result[a-1][b-1] + tree_result[a][b]
        if len(tree[a-1]) == b:
            result_b = 0
        else:
            result_b = tree_result[a-1][b] + tree_result[a][b]
        if result_a > result_b:
            tree_result[a][b] = result_a
        else:
            tree_result[a][b] = result_b

print(tree_result)
print(max(tree_result[len(tree)-1]))