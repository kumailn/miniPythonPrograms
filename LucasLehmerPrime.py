#Lucas–Lehmer prime number test for p > 3
#Returns false if a number is not prime or not mersenne prime. 
def lp(p):
    mp = 0
    for i in range(30):
        if p == (2 ** i) - 1:
          mp = i
    #print(mp)
    l = [4]
    for i in range(18):
        l += [(l[i] ** 2) - 2]
    #print(l[mp-2])
    if l[mp-2] % p == 0:
        return True
    return False
    print(l)
