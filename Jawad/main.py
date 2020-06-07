import requests
from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString

import os
#from test_nltk import decouper, afficher

def decouper(texte):
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
    plt.savefig( nom_dossier +"/"+ nom_image )
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

def occurences_emotions(mots):
    emotions = ["amour", "colere", "degout", "honte", "joie", "peur", "surprise", "tristesse"]
    dictionnaire  = {}
    ensemble = set()
    for emotion in emotions :
        dictionnaire[emotion] = 0
        with open("../emotions/"+ emotion +".txt", "r", encoding="utf-8") as fichier :
            for mot in fichier :
                if mot.strip() in mots:
                    dictionnaire[emotion]+= 1
                    ensemble.add( mot.strip() )
        print(mots)
    print("ensemble :", ensemble)
    return dictionnaire

def extraire_genius(url):
    from pathlib import Path

    soup = rechercher_page(url)
    liste_paroles = recuperer_paroles(soup)

    titre   = soup.find(class_="SongHeader__Title-sc-1b7aqpg-7").text.strip()
    artiste = soup.find(class_="SongHeader__Artist-sc-1b7aqpg-8").text.strip()

    print("titre :", titre )
    print("artiste :", artiste )

    print("File      Path:", Path(__file__).absolute())
    print("Directory Path:", Path().absolute())

    if not os.path.exists(artiste):
        os.mkdir(artiste)

    with open( artiste+"/"+titre+".txt", 'w+', encoding="utf-8") as fichier:
        for ligne in liste_paroles : fichier.write(ligne+"\n")

    mots = []
    for ligne in liste_paroles: mots += decouper(ligne)

    afficher( occurences_emotions(mots), nom_dossier=artiste, nom_image=titre)

    #from nltk.corpus import stopwords
    #print("stopwords: ", stopwords.words("french") )

def rechercher_genius(artiste):
    url = "https://genius.com/search?q="+artiste
    print(f"rechercher({artiste})genius...", url )
    texte_html = requests.get(url).text
    soup = BeautifulSoup(texte_html, "lxml")
    with open( artiste +".html", 'w+', encoding="utf-8") as file: file.write(str(soup))
'''
    while True :
        texte_html = requests.get(url).text
        soup = BeautifulSoup(texte_html, "lxml")
        if soup.find("div", {"id": "application"})!=None:
            with open( artiste +".html", 'w+', encoding="utf-8") as file: file.write(soup)
            return soup
'''
def trier_fichier(nom_fichier):
    with open(nom_fichier, "r", encoding="utf-8") as fichier:
        lignes = [ligne.strip() for ligne in fichier]

    with open("sorted_"+nom_fichier, "w+", encoding="utf-8") as fichier:
        lignes.sort()
        for ligne in lignes : fichier.write(ligne+"\n")

jacques_brel = [
    "https://genius.com/Jacques-brel-la-valse-a-mille-temps-lyrics"
]



"https://genius.com/Keenv-les-mots-lyrics"

'''
liste = extraire_genius(
    "https://genius.com/Keenv-explique-moi-lyrics"
)
'''
