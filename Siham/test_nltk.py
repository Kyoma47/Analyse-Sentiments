from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nomFichier = "trois_petites_oies.txt"
with open("textes/"+ nomFichier, "r", encoding='utf-8') as fichier:
        texte = fichier.read()
        texte_propre = texte.lower().translate( str \
        .maketrans('’\n\t-',4*' ', string.punctuation.replace('-','') + '…0123456789' ) )
        mots = word_tokenize(texte_propre, "french")
        mots_utiles = [mot for mot in mots if mot not in stopwords.words("french")]
        print(mots_utiles)
