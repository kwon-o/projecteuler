def Triangle_list():
    triangle_list = []
    for i in range(285,100000):
        triangle_list.append((i * (i + 1)) / 2)
    return triangle_list

def Pentagonal_list():
    pentagonal_list = []
    for i in range(165,100000):
        pentagonal_list.append(  (i * (3 * i - 1 )) / 2)
    return  pentagonal_list

def Hexagonal_list():
    hexagonal_list = []
    for i in range(143,100000):
        hexagonal_list.append( i * ( 2 * i - 1 ) )
    return hexagonal_list


tri = Triangle_list()
pen = Pentagonal_list()
hexa = Hexagonal_list()

for t in tri:
    if t in pen and t in hexa:
        print(t)
