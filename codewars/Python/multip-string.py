def soliution(n,x):
    contadorDaQnt, contadorDoLoop=int(1)
    multiplosLista=[]
    while contadorDaQnt<n:
        if contadorDoLoop % x == 0:
            multiplosLista.append(contadorDoLoop)
            contadorDaQnt+=1
        contadorDoLoop+=1
    return multiplosLista