import math
from decimal import *
s = 15
# s = 1000000000000

while True:
    Dsq = 1 + ( 2 * s * (s-1))
    D1 = str(Decimal(math.sqrt(Dsq)))
    # print(D1)
    if "." not in D1 :
        D = Decimal(math.sqrt(Dsq))
        b = ((1 + D) / 2)
        p = (b / s) * ((b-1) / (s-1))
        print(p, b, s)
        # break
    s += 1
