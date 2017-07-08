

def f(n):
    l = []
    start, stop = -100, 100
    for i in range(start, stop + 1):
        print(i)
        for j in range(start, stop + 1):
            for k in range(start, stop + 1):
                if n == (i**3 + j**3 + k**3):
                    l = [i, j, k]
                    print(l)
                    #return 1
    return ("end")
    
