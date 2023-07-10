def move_zeros(lst):
    listaZeros=[]
    listaNaoZeros=[]
    for i in range(len(lst)):
        number=lst[i]
        if number == 0:
            lst.append(listaZeros.pop(i))
        else:
            lst.append(listaNaoZeros(i))
    return listaNaoZeros + listaZeros