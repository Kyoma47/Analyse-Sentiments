def nettoyer(texte): #tokenization
    return texte.translate(
        str.maketrans('’',' ', string.punctuation + '…\t\n' )
    )

def decouper(texte): #texte sans ponctuation
    return texte.split()

def occurences(liste_mots):
    D = {}
    for mot in liste_mots:
        D[mot.lower()] = 1 if mot.lower() not in D else D[mot.lower()]+1
    return D
