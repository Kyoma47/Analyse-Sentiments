import requests
from bs4 import BeautifulSoup
import bs4.element
import os
from pathlib import Path
from main_nltk import decouper, afficher
import matplotlib.pyplot as plt

def rechercher_page(url):
    print("genius...", url.split("/")[3] )
    while True:
        texte_html = requests.get(url).text
        soup = BeautifulSoup(texte_html, 'lxml')
        if soup.find("div", {"id": "application"}) != None :
            return soup

def recuperer_paroles(soup):
    lignes = []
    for div in soup.find_all(class_="Lyrics__Container-sc-1ynbvzw-2") :
        for element in div:
            if element.find("span") not in [-1, None] :
                lignes += [ str(e) for e in element.find("span") if type(e)==bs4.element.NavigableString ]
            elif type(element) != bs4.element.Tag :
                lignes += [str(element)]
    return lignes

def occurences_emotions(mots):
    emotions = ["amour", "colere", "degout", "honte", "joie", "peur", "surprise", "tristesse"]
    dictionnaire = {}
    ensemble = set()
    for emotion in emotions:
        dictionnaire[emotion] = 0
        with open("emotions/" + emotion + ".txt", "r", encoding='utf-8') as fichier :
            for mot in fichier:
                if mot.strip() in mots :
                    dictionnaire[emotion] +=1
                    ensemble.add(mot.strip())
    return dictionnaire

def afficher(dic_emotions, nom_dossier = "graphes", nom_image = "graphe.png"):
    w = dic_emotions
    fig, axl = plt.subplots()
    plt.bar( w.keys(), w.values() )
    fig.autofmt_xdate()
    plt.savefig(nom_dossier + "/" + nom_image)
    #plt.show()
    print(w)

def extraire_genius(url):
    soup = rechercher_page(url)
    liste_paroles = recuperer_paroles(soup)
    titre = soup.find(class_="SongHeader__Title-sc-1b7aqpg-7").text
    artiste = soup.find(class_="SongHeader__Artist-sc-1b7aqpg-8").text
    nomDossier = 'Siham/' + artiste
    if not os.path.exists(nomDossier):
        os.mkdir(nomDossier)
    with open(nomDossier + "/"+ titre + ".txt", "w+", encoding='utf-8') as fichier :
        for ligne in liste_paroles :
            fichier.write(ligne+"\n")
    mots = []
    for ligne in liste_paroles :
        mots += decouper(ligne)
    afficher(occurences_emotions(mots), nomDossier, titre)

Kennv = ["https://genius.com/Keenv-explique-moi-lyrics", "https://genius.com/Keenv-les-mots-lyrics", \
"https://genius.com/Keenv-saltimbanque-lyrics", "https://genius.com/Keenv-ma-vie-au-soleil-lyrics"]

Lara_fabian = ["https://genius.com/Lara-fabian-par-amour-lyrics", "https://genius.com/Lara-fabian-je-taime-lyrics", \
"https://genius.com/Lara-fabian-papillon-lyrics", "https://genius.com/Lara-fabian-changer-le-jeu-lyrics", \
"https://genius.com/Lara-fabian-immortelle-lyrics", "https://genius.com/Lara-fabian-pardonne-lyrics", \
"https://genius.com/Lara-fabian-sen-aller-lyrics", "https://genius.com/Lara-fabian-que-jetais-belle-lyrics"]

Florent_Pagny = ["https://genius.com/Florent-pagny-vieillir-avec-toi-lyrics", "https://genius.com/Florent-pagny-souviens-toi-lyrics", \
"https://genius.com/Florent-pagny-condoleances-lyrics", "https://genius.com/Florent-pagny-le-present-dabord-lyrics", \
"https://genius.com/Florent-pagny-je-connais-personne-lyrics", "https://genius.com/Florent-pagny-noir-et-blanc-lyrics", \
"https://genius.com/Florent-pagny-rafale-de-vent-lyrics", "https://genius.com/Florent-pagny-revenons-sur-terre-lyrics"]

chanteurs = [Florent_Pagny, Lara_fabian, Kennv]

for chanteur in chanteurs:
    for chanson in chanteur:
        extraire_genius(chanson)
