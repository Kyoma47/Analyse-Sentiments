import requests
from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString

import os
#from test_nltk import decouper, afficher

def decouper(texte):
    import string
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords

    a_remplacer = '´’-\n\t' + string.punctuation
    minuscules = texte.lower()
    propre = minuscules.translate( str.maketrans(a_remplacer, len(a_remplacer)*' ', '…0123456789') )
    mots = word_tokenize( propre, "french")
    return [mot for mot in mots if mot not in stopwords.words("french")]

def afficher(dic_emotions, nom_dossier="ghraphes", nom_image="graph.png" ):
    from collections import Counter
    import matplotlib.pyplot as plt

    w = dic_emotions
    fig, axl = plt.subplots()
    plt.bar( w.keys(), w.values() )
    fig.autofmt_xdate()
    plt.savefig( nom_dossier +"/"+ nom_image +".png" )
    #plt.show()
    print(w)

def rechercher_page(url):
    print("genius...", url.split("/")[3] )
    while True :
        texte_html = requests.get(url).text
        soup = BeautifulSoup(texte_html, "lxml")
        if soup.find("div", {"id": "application"})!=None: return soup

def recuperer_paroles(soup):
    lignes = []
    for div in soup.find_all(class_="Lyrics__Container-sc-1ynbvzw-2"):
        for element in div:
            span = element.find("span")
            if span not in [-1, None]:
                lignes += [ str(e) for e in span if type(e)==NavigableString ]
            elif type(element)!= Tag : lignes += [str(element)]
    return lignes


ignores = set()
def occurences_emotions(mots):
    global ignores
    emotions = ["amour", "colere", "degout", "honte", "joie", "peur", "surprise", "tristesse"]
    dictionnaire  = {}
    utilises = set()
    for emotion in emotions :
        dictionnaire[emotion] = 0
        with open("../emotions/"+ emotion +".txt", "r", encoding="utf-8") as fichier :
            for mot in fichier :
                if mot.strip() in mots:
                    dictionnaire[emotion]+= 1
                    utilises.add( mot.strip() )

    ignores = ignores.union( set(mots)-set(utilises) )
    print("utilisés :", utilises)
    #print("ignorés  :", ignores )
    return dictionnaire

def extraire_genius(url):
    from pathlib import Path
    soup = rechercher_page(url)
    liste_paroles = recuperer_paroles(soup)

    titre   = soup.find(class_="SongHeader__Title-sc-1b7aqpg-7").text.strip()
    artiste = soup.find(class_="SongHeader__Artist-sc-1b7aqpg-8").text.strip()

    print("titre :", titre )
    print("artiste :", artiste )

    if not os.path.exists(artiste): os.mkdir(artiste)

    with open( artiste+"/"+titre+".txt", 'w+', encoding="utf-8") as fichier:
        for ligne in liste_paroles : fichier.write(ligne+"\n")

    mots = []
    for ligne in liste_paroles: mots += decouper(ligne)

    afficher( occurences_emotions(mots), nom_dossier=artiste, nom_image=titre)
    print()
    #from nltk.corpus import stopwords
    #print("stopwords: ", stopwords.words("french") )


def trier_fichier(nom_fichier):
    with open(nom_fichier, "r", encoding="utf-8") as fichier:
        lignes = [ligne.strip() for ligne in fichier]

    with open("sorted_"+nom_fichier, "w+", encoding="utf-8") as fichier:
        lignes.sort()
        for ligne in lignes : fichier.write(ligne+"\n")

def traiter_target(separement=True):
    global ignores
    with open("targets.txt", "r", encoding="utf-8") as file:
        for lien in file:
            if len(lien)>1: extraire_genius(lien.strip())

    ignores = list( ignores )
    ignores.sort()
    with open("mots_ignores.txt", "w+", encoding="utf-8") as file:
        for mot in ignores: file.write(mot+"\n")

traiter_target()
