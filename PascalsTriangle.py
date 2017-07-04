#Pascals Triangle, returns Pascals triangle with a height of h
import math

def ncr(n,r):
    return math.factorial(n) / math.factorial(r) / math.factorial(n-r)


def p(h):
    l = []
    l2 = []
    for i in range(h):
        #print("i " + str(i))
        l2 = []
        for j in range(i + 1):
            #print(j)
            l2 += [ncr(i, j)]
        l += [l2]
    for i in l:
        print(i)

    
