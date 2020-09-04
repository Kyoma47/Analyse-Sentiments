from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import string
import matplotlib.pyplot as plt
import math
import numpy as np
import glob

def decouper_texte(texte, n=10):
    # Calculer la longueur du texte, la taille de chaque partie et la position de départ de celle ci.
    longueur = len(texte)
    taille = math.floor(longueur / n)
    depart = np.arange(0, longueur, taille)

    #Tirer des morceaux de texte de taille égale et les mettre dans une liste
    liste_decoupee = []
    for partie in range(n):
        liste_decoupee.append(texte[depart[partie]:depart[partie]+taille])
    return liste_decoupee

#On découpe le texte en 10 parties et on calcule pour chaque partie la polarité associée
#pour enfin dessiner l'evolution de la polarité dans le temps

for fichier in glob.glob("Chansons/**/*.txt",recursive=True) :
    texte = open( fichier, 'r', encoding="utf-8").read()
    parties = decouper_texte(texte)
    polarite_parties = []
    for p in parties:
        polarite_parties.append(TextBlob(p,pos_tagger=PatternTagger(),analyzer=PatternAnalyzer()).sentiment[0])
    nom= fichier.split("\\")
    nom_chanson =nom[2].split(".")
    plt.plot(polarite_parties)
    plt.title(nom_chanson[0])
    plt.show()
