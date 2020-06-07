import requests
from bs4 import BeautifulSoup
from bs4.element import Tag as tg
import pickle
from test_nltk import decouper, afficher


def scraping_genius(url):
    print("while!")
    while True:
        page = requests.get(url).text
        soup = BeautifulSoup(page, "lxml")
        div  = soup.find(class_="Lyrics__Container-sc-1ynbvzw-2 jgQsqn")
        if div!=None: return [str(ligne) for ligne in div if type(ligne) != tg]
        #div  = soup.find(class_="song_body-lyrics")

def mots_genius(url):
    mots = []
    for ligne in scraping_genius(url): mots += decouper(ligne)
    return mots

def emotions(url):
    mots = mots_genius(url)
    dic = {}
    for emotion in ["amour", "colere", "degout", "honte", "joie", "peur", "surprise", "tristesse"]:
        dic[emotion] = 0
        with open("../emotions/"+ emotion +".txt", "r", encoding="utf-8") as fichier :
            for mot in decouper(fichier.read()):
                if mot in mots:
                    print(emotion, ":", mot)
                    dic[emotion]+= 1
                else : print(mot)
    print("mots inutilisees : ", set(mot for mot in mots))
    afficher( dic )

urls = [
    "https://genius.com/Keenv-les-mots-lyrics"
    "https://genius.com/Damso-feu-de-bois-lyrics",
    "https://genius.com/Damso-amnesie-lyrics",
    "https://genius.com/Damso-macarena-lyrics",
    "https://genius.com/Damso-mosaique-solitaire-lyrics",
    "https://genius.com/Damso-n-j-respect-r-lyrics"
]

def boucle_genius(urls):
        for url in urls :
            while True:
                page = requests.get(url).text
                soup = BeautifulSoup(page, "lxml")
                print(url.split("/")[3])
                artiste = soup.find(class_="Link-h3isu4-0 dpVWpH SongHeader__Artist-sc-1b7aqpg-8 DYpgM")
                #artiste = soup.find(class="Link-h3isu4-0 dpVWpH SongHeader__Artist-sc-1b7aqpg-8 DYpgM")
                titre = soup.find(class_="SongHeader__Title-sc-1b7aqpg-7 jQiTNQ")
                #titre = soup.find(class_="SongHeader__Title-sc-1b7aqpg-7 eJWiuG")
                print("Atiste :", artiste, "Titre :", titre)
                if artiste != titre != None : break


boucle_genius(urls)

#afficher(mots_genius(url))
#emotions(url)
