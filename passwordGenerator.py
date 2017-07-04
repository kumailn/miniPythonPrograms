from random import randint
#Password generator

def generate(length):
    a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$&"
    s = ""
    for i in range(length):
        s += a[randint(0, len(a) - 1)]
    return s
        
