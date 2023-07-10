def add_binary(a,b):
    soma = int(a) + int(b)

    binario = []
    while soma >= 1:
        binario.append(soma % 2) 
        soma//=2

    binarioFim=binario[::-1]
    resposta = int(''.join(map(str, binarioFim)))
    return resposta 
