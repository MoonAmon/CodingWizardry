def add_binary(n):

    binario = []
    while n >= 1:
        binario.append(n % 2) 
        n//=2

    binarioFim=binario[::-1]
    for i in binarioFim:
        resposta+=i
    return resposta 
