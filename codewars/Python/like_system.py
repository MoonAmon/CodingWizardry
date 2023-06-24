def likes(names):
    if len(names)==0:
        frase = "no one likes this"
        return frase
    elif len(names)==1:
        frase = "{} likes this".format(names[0])
        return frase
    elif len(names)==2:
        frase = "{} and {} like this".format(names[0],names[1])
        return frase
    elif len(names)==3:
        frase = "{}, {} and {} like this".format(names[0],names[1],names[2])
        return frase
    elif len(names)>3:
        tamanho=len(names)-2
        frase = "{}, {} and {} others like this".format(names[0],names[1],tamanho)
    pass