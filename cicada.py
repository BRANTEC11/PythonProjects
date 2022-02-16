def cic(x):
    a = 17
    b = 13
    c = 4
    aa = 2021
    bb = 2015
    cc = 2019
    aL = []
    bL = []
    cL = []
    if x == 0:
        while aa >= a:
            aa -= 17
            aL.append(aa)
    elif x == 1:
        while bb >= b:
            bb -= 13
            aL.append(bb)
    elif x == 2:
        while cc >= c:
            cc -= 4
            aL.append(cc)
    return aL
def common_member(a, b, c):
    a_set = set(a)
    b_set = set(b)
    c_set = set(c)
    print(a_set & b_set & c_set)
    

print(common_member(cic(0),cic(1), cic(2)))
