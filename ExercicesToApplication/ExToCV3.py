from decimal import *
def generateNUmbers(od, do,skok):
    l=[]
    i= Decimal(od)
    while i < do:
        i+=Decimal(skok)
        l.append(i)
    print(l)





