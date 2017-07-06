def collatz(n):
    l = []
    while (n != 1):
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
        l += [n]
    print(l)
    print(str(len(l)) + " steps")
