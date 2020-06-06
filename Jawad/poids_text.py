
def nettoyer(texte): #tokenization
    import string
    return texte.translate(
        str.maketrans('’\n','  ', string.punctuation + '…\t' )
    )

def decouper(texte): #texte sans ponctuation
    return texte.split()

def trier(liste_mots):
    liste_mots.sort()

def occurences(liste_mots):
    D = {}
    for mot in liste_mots:
        D[mot.lower()] = 1 if mot.lower() not in D else D[mot.lower()]+1
    return D

def doublons(nom_fichier):
    with open(nom_fichier, "r", encoding="utf-8" ) as fichier :
        mots = decouper( nettoyer( fichier.read() ) )
        trier(mots)
        dic  = occurences( mots )
        for cle in dic :
            if dic[cle]>1 : print(cle, ":", dic[cle])

def alphabetic_fichier(nom_fichier):
    with open(nom_fichier, "r", encoding="utf-8" ) as fichier :
        mots = decouper( nettoyer( fichier.read() ) )
        trier(mots)
        with open("alphabetic_"+ nom_fichier.split("/")[-1], 'w+', encoding="utf-8") as file:
            file.write('\n')
            for mot in mots: file.write( mot +'\n')

def afficher(list_emotions, nom_image="graph.png" ):
    from collections import Counter
    import matplotlib.pyplot as plt

    w = Counter(list_emotions)
    fig, axl = plt.subplots()
    plt.bar( w.keys(), w.values() )
    fig.autofmt_xdate()
    plt.savefig( nom_image )
    plt.show()
    print(w)

def poid_texte(nom_fichier):
    emotions = ["amour", "colere", "degout", "honte", "joie", "peur", "surprise", "tristesse" ]
    with open("../textes/" + nom_fichier, "r", encoding="utf-8") as texte:
        mots = decouper( nettoyer( texte.read() ) )

    print("mots :", mots)
    liste_emotions = []
    for emotion in emotions :
        with open("../emotions/"+ emotion +".txt", encoding="utf-8") as fichier :
            for mot in fichier:
                #print(f"'{mot[:-1].strip()}'")
                if mot[:-1].strip() in mots :
                    liste_emotions.append( emotion )
        print(emotion, liste_emotions)

    afficher(liste_emotions)
