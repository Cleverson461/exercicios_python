def tras_frente(text):
    text = text[::-1]
    return text


def indice_par(text):
    text = text[::2] # 0 2 4 6 8 
    return text

def indice_impar(text):
    text = text[1::2]
    return text