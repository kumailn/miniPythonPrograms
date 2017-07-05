#Lucas Numbers

def p(n):
    l = [2,1]
    for i in range(n):
        l += [l[i] + l[i+1]]
    print(l)
