#Calculates the value of the Riemann Zeta function at S up to an accuracy of n terms.
import decimal

def zeta(s, n):
    a = decimal.Decimal("0." + (15 * "0"))
    for i in range(1, n + 1):
        a += 1/( decimal.Decimal(str(i)) ** s)
    print(a)
        
