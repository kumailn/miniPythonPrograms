from BruteforcePrimeCheck import p
from random import randint

def g(n):
    x = randint(int("1" + ("0"* (n - 1))), int("9"*n))
    while p(x) == False:
        x = x + 1
    return x
