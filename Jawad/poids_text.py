
def nettoyer(texte): #tokenization
    import string
    return texte.translate(
        str.maketrans('’\n','  ', string.punctuation + '…\t' )
    )

def decouper(texte): #texte sans ponctuation
    return texte.split()

def occurences(liste_mots):
    D = {}
    for mot in liste_mots:
        D[mot.lower()] = 1 if mot.lower() not in D else D[mot.lower()]+1
    return D

def occurences_fichier(nom_fichier):
    with open(nom_fichier, "r", encoding="utf-8" ) as fichier :
        dic = occurences( decouper( nettoyer( fichier.read() ) ) )
        for cle in dic :
            if dic[cle]>1 : print(cle, ":", dic[cle])
