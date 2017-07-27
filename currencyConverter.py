from decimal import Decimal
from forex_python.converter import CurrencyRates
cc = CurrencyRates()

def toUSD(a):
    #Converts CAD to USD
    return(cc.convert("CAD", "USD", Decimal(a)))

print(toUSD(170))