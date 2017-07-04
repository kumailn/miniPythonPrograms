#Exprimentally calculates the Riemann Zeta function at 2, 3 and 4 using Eulers coprime conjecture 
from math import gcd as bltin_gcd
from random import randint


def coprime2(a, b, c):
    return bltin_gcd(c, bltin_gcd(a, b)) == 1

def coprime3(a, b, c, d):
    return bltin_gcd(d, bltin_gcd(c, bltin_gcd(a, b))) == 1

def cns1(s):
    l = []
    for i in range(s):
        l += [[randint(0, 10000), randint(0, 10000)]]
    c = 0
    for i in range(len(l)):
        if bltin_gcd(l[i][0], l[i][1]) == True:
            c += 1
    l2 = [len(l), c, len(l)/c]
    #print(l)
    return l2

def cns(s):
    l = []
    for i in range(s):
        l += [[randint(0, 10000), randint(0, 10000),randint(0, 10000)]]
    c = 0
    for i in range(len(l)):
        if coprime2(l[i][0], l[i][1], l[i][2]) == True:
            c += 1
    l2 = [len(l), c, len(l)/c]
    print(l)
    return l2

def cns2(s):
    randSample = 1000000
    l = []
    for i in range(s):
        l += [[randint(0, randSample), randint(0, randSample),randint(0, randSample), randint(0, randSample)]]
    c = 0
    for i in range(len(l)):
        if coprime3(l[i][0], l[i][1], l[i][2], l[i][3]) == True:
            c += 1
    l2 = [len(l), c, len(l)/c]
    return l2



def zeta(s, size):
    c = 1
    for i in range(1, size + 1):
        c += (1/size ** s)
    return c
