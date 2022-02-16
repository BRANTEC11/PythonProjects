#For use in MA232 (Linear Algebra)
def det33(a,b,c,d,e,f,g,h,i):
    ans = (a*((e*i)-(f*h)))-(b*((d*i)-(f*g)))+(c*((d*h)-(e*g)))
    return ans

def det22(a,b,c,d):
    ans = (a*d)-(c*b)
    return ans