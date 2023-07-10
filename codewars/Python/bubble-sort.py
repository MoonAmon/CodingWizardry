def descending_order(num):
    listaDigitos = [int(digito) for digito in str(num)]
    fim = len(listaDigitos)
    
    while fim > 1:
        trocou = False
        x = 0
        
        while x < (fim-1):
            if listaDigitos[x] < listaDigitos[x+1]:
                trocou = True
                temp = listaDigitos[x]
                listaDigitos[x] = listaDigitos[x+1]
                listaDigitos[x+1] = temp
            x += 1
        
        if not trocou:
            break
        
        fim -= 1
    
    return int(''.join(map(str, listaDigitos)))
