import requests
from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString

import os
from test_nltk import decouper, afficher

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

    print(mots)

    #from nltk.corpus import stopwords
    #print("stopwords: ", stopwords.words("french") )


urls = [
    "https://genius.com/Damso-mosaique-solitaire-lyrics",
    "https://genius.com/Keenv-les-mots-lyrics",
    "https://genius.com/Jacques-brel-la-valse-a-mille-temps-lyrics",
    "https://genius.com/Damso-feu-de-bois-lyrics",
    "https://genius.com/Damso-amnesie-lyrics",
    "https://genius.com/Damso-macarena-lyrics",
    "https://genius.com/Damso-n-j-respect-r-lyrics"
]

liste = extraire_genius(
    "https://genius.com/Keenv-explique-moi-lyrics"
)
