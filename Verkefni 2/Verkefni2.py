



#2
"""
def summa(n):
    if n == 1:
        return 1
    else:
        return n**2 + summa(n-1)
print(summa(5))
"""

#3
"""
def runa(n):
    if n==1:
        print(1," ")
    else:
        summa = n
        for x in range(n-1):
            summa += n-(x+1)
        runa(n-1)
        print(summa)

print(runa(6))
"""

#4
"""
def þversumma(n):
    n = str(n)
    if n == "":
        return 0
    else:
        return int(n[0]) + int(þversumma(n[1:]))

print(þversumma(1234))
"""

#5

def samnefnari(n,m):
    t = 0
    if n > m:
        t = m
    else:
        t = m
    while True:
        if m%t == 0 and n%t == 0:
            return t
            break
        else:
            t-=1

print(samnefnari(8,12))




