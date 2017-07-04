#Brute force prime checker

def p(n):
    for i in range(1, n):
        if i != 1:
            if n % i == 0:
                return False
    return True
