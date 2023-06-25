def make_readable(seconds):
    hour = seconds // 3600
    secondsMid = seconds % 3600
    minutes = secondsMid // 60
    secondsFinal = secondsMid % 60
    
    resposta = "{:02}:{:02}:{:02}".format(hour,minutes,secondsFinal)
    return resposta