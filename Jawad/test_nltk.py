from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords

nom_fichier = "trois_petites_oies"

def afficher(liste, nom_image="graph.png"):
    from collections import Counter
    import matplotlib.pyplot as plt
    
    w = Counter(liste)
    fig, axl = plt.subplots()
    plt.bar( w.keys(), w.values() )
    fig.autofmt_xdate()
    plt.savefig( nom_image )
    plt.show()
    print(w)

def decouper(texte):
    a_remplacer = '’-\n\t' + string.punctuation
    minuscules = texte.lower()
    propre = minuscules.translate( str.maketrans(a_remplacer, len(a_remplacer)*' ', '…0123456789') )
    mots = word_tokenize( propre, "french")
    return [mot for mot in mots if mot not in stopwords.words("french")]

def traiter_fichier(texte):
    with open("../textes/"+ nom_fichier +".txt", "r", encoding="utf-8") as fichier:
        afficher( decouper( fichier.read() ) )
