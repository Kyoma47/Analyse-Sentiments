import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import glob
import string

def nettoyer_donnees(nomFichier) :
    texte = open(nomFichier, encoding='utf-8').read().lower()
    texte_propre = texte.translate( str\
    .maketrans('’\n\t-',4*' ', string.punctuation + '…0123456789'+"«»"))
    mots = word_tokenize(texte_propre, "french")
    mots_utiles = [mot for mot in mots if mot not in stopwords.words("french")]
    return mots_utiles


def Emotions_Extraction(donnees) :
    emotions = {"amour":0,"colere":0,"honte":0,"degout":0,"peur":0,"surprise":0,"tristesse":0,"joie":0}
    for emotion in emotions :
        with open('emotions/'+ emotion +'.txt',encoding="utf-8") as fichier :
            for mot in fichier :
                mot = mot.replace('\n','')
                if mot in donnees :
                    emotions[emotion]+=1
    return emotions


def Emotions_Representation(emotions,nomChanson) :
    couleurs = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red','green','gray',"blue"]
    patchs, textes = plt.pie(list(emotions.values()), colors=couleurs, shadow=True, startangle=90)
    plt.legend(patchs, list(emotions.keys()), loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.title(nomChanson)
    plt.show()


for fichier in glob.glob("Chansons/**/*.txt",recursive=True) :
    texte_nettoye = nettoyer_donnees(fichier)
    nom= fichier.split("\\")
    nom_chanson =nom[2].split(".")
    Emotions_Representation(Emotions_Extraction(texte_nettoye),nom_chanson[0])
