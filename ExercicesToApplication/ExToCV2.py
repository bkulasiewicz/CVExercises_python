def addElementsNotIn(lista,n):

    listToCompare = []
    for i in range(1,n+1):
        listToCompare.append(i)
    for i in lista:
        listToCompare.remove(i)

    print(listToCompare)
