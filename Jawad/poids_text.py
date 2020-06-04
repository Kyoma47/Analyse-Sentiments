
def occurence(texte):
    mots = text.split()
    D = {}
    for mot in mots:
        D[mot] = 0 if mot not in mots else D[mot]+1
    return D
