def incr(n):
    incrlist = list(str(n))
    for i in range(0, len(incrlist)-1):
        if int(incrlist[i]) < int(incrlist[i+1]):
            return False
            break
    return True

def decr(n):
    incrlist = list(str(n))
    for i in range(0, len(incrlist)-1):
        if int(incrlist[i]) > int(incrlist[i+1]):
            return False
            break
    return True

def bouncy(n):
    if incr(n)==False and decr(n)==False:
        return True
    else:
        return False

cnt = 0
n = 799000
while (float(cnt)/n) < 0.99:
    cnt = 0
    for i in range(0,n):
        if bouncy(i) == True:
            cnt += 1
    try:
        print (n, cnt, (float(cnt)/n))
    except ZeroDivisionError:
        pass
    n += 1
