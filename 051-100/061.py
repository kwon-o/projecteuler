'''
Triangle 45 - 140
Square 32 - 99
Pentagonal 26 - 81
Hexagonal 23 - 70
Heptagonal 21 - 63
Octagonal 19 - 58'''
import copy

def Triangle_list():
    triangle_list = []
    for i in range(45,141):
        triangle_list.append((i * (i + 1)) / 2)
    return triangle_list

def Square_list():
    square_list = []
    for i in range(32,100):
        square_list.append(i * i)
    return square_list

def Pentagonal_list():
    pentagonal_list = []
    for i in range(26,82):
        pentagonal_list.append(  (i * (3 * i - 1 )) / 2)
    return  pentagonal_list

def Hexagonal_list():
    hexagonal_list = []
    for i in range(23,71):
        hexagonal_list.append( i * ( 2 * i - 1 ) )
    return hexagonal_list

def Heptagonal_list():
    heptagonal_list = []
    for i in range(21,64):
        heptagonal_list.append( ( i * ( 5 * i - 3 ) ) / 2 )
    return heptagonal_list

def Octagonal_list():
    octagonal_list = []
    for i in range(19,59):
        octagonal_list.append( i * ( 3 * i - 2 ) )
    return octagonal_list

all_list = [Triangle_list(), Square_list(), Pentagonal_list(), Hexagonal_list(), Heptagonal_list(), Octagonal_list()]
all_dic = {'tri' : all_list[0],
           'squ' : all_list[1],
           'pen' : all_list[2],
           'hex' : all_list[3],
           'hep' : all_list[4],
           'oct' : all_list[5]}

def finder(list_finder):
    finder_AllList = []
    for i in list_finder:
        finder_dic = copy.deepcopy(i[2])
        del finder_dic[i[0]]
        for j in finder_dic.keys():
            for k in finder_dic[j]:
                finder_list = []
                finder_sumList = i[3]
                finder_sumNum = i[4]
                if str(i[1])[2:4] == str(k)[0:2]:
                    finder_list.append(j)
                    finder_list.append(k)
                    finder_list.append(finder_dic)
                    finder_list.append(finder_sumList + '/' + j + "(" + str(k) + ")")
                    finder_list.append(finder_sumNum + k)
                    finder_AllList.append(finder_list)
    return finder_AllList

for o in all_dic.keys():
    for p in all_dic[o]:
        sum_list = o + "(" + str(p) + ")"
        sum_num = 0
        sum_num += p
        list1 = [[o, p, all_dic, sum_list, sum_num]]
        if finder(finder(finder(finder(finder(list1))))) != []:
           for q in finder(finder(finder(finder(finder(list1))))):
               if str(p)[0:2] == str(q[1])[2:4]:
                   print(q[3],q[4])