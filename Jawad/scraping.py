import requests
from bs4 import BeautifulSoup
from bs4.element import Tag as tg
import pickle
from test_nltk import decouper, afficher

from nltk.corpus import stopwords

def trouver_page_genius(url):
    print("genius...", url.split("/")[3] )
    while True:
        page = requests.get(url).text
        soup = BeautifulSoup(page, "lxml")
        if soup.find("div", {"id": "application"})!=None: return soup

def recuperer_texte(soup):
    conteneurs  = soup.find_all(class_="Lyrics__Container-sc-1ynbvzw-2")
    lignes = []
    for conteneur in conteneurs :
        lignes += [ str(contenu) for contenu in conteneur if type(contenu)!=tg ]
    return lignes

def scraping_genius(url):
    soup = trouver_page_genius(url)
    titre   = soup.find(class_="SongHeader__Title-sc-1b7aqpg-7").text.strip()
    artiste = soup.find(class_="SongHeader__Artist-sc-1b7aqpg-8").text.strip()
    print(f"titre   : '{titre}'")
    print(f"artiste : '{artiste}'")

    nom_dossier = artiste
    nom_fichier = titre + ".txt"

    #a tester !!!
    if not os.path.exists(nom_dossier):
        os.makedirs(nom_dossier)

    lignes = recuperer_texte(soup)

    mots = []
    for ligne in lignes: mots += decouper(ligne)

    emotions = ["amour", "colere", "degout", "honte", "joie", "peur", "surprise", "tristesse"]
    mots_comptes = set()
    occurences_emotions = { cle:0 for cle in emotions}

    for emotion in occurences_emotions :
        #dic[emotion] = 0
        with open("../emotions/"+ emotion +".txt", "r", encoding="utf-8") as fichier :
            for mot in decouper(fichier.read()):
                if mot in mots:
                    print(emotion, ":", mot)
                    mots_comptes.add( mot )
                    occurences_emotions[emotion]+= 1

    afficher(occurences_emotions)
    print("texte : ", lignes )
    print("mots : ", mots)
    print("mots utilisees   : ", mots_comptes)
    print("mots inutilisees : ", set(mots)-mots_comptes)

    return set(mot for mot in mots)

def imprimer(liste_lignes):
    print("debut texte {"+ 50*"_")
    for ligne in liste_lignes : print(ligne)
    print("fin texte   }"+ 50*"_")

urls = [
    "https://genius.com/Damso-mosaique-solitaire-lyrics",
    "https://genius.com/Keenv-les-mots-lyrics",
    "https://genius.com/Jacques-brel-la-valse-a-mille-temps-lyrics",
    "https://genius.com/Damso-feu-de-bois-lyrics",
    "https://genius.com/Damso-amnesie-lyrics",
    "https://genius.com/Damso-macarena-lyrics",
    "https://genius.com/Damso-n-j-respect-r-lyrics"
]
liste = recuperer_texte( trouver_page_genius(urls[1]) )
imprimer(liste)
#liste = scraping_genius(urls[1])
