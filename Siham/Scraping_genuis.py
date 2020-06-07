import requests
from bs4 import BeautifulSoup
from bs4.element import Tag as tg
import pickle
from main_nltk import decouper, afficher

def scraping_genius(url):
    while True:
        page = requests.get(url).text
        soup = BeautifulSoup(page, "lxml")
        div = soup.find(class_="Lyrics__Container-sc-1ynbvzw-2 jgQsqn")
        if div != None:
            return [str(ligne) for ligne in div if type(ligne) != tg]

def mots_genius(url):
    list = []
    for ligne in scraping_genius(url):
        list += decouper(ligne)
    return list

def emotions(url, titre, artiste):
    mots_finals = mots_genius(url)
    dic = {}
    for emotion in ["amour", "colere", "degout", "honte", "joie", "peur",\
     "surprise", "tristesse"]:
        dic[emotion] = 0
        with open("../emotions/"+ emotion + ".txt", "r", encoding='utf-8') as fichier:
            for mot in decouper(fichier.read()):
                if mot in mots_finals :
                    dic[emotion] += 1
    afficher(dic, titre, artiste)

urls = ["https://genius.com/Keenv-explique-moi-lyrics", "https://genius.com/Keenv-les-mots-lyrics", \
"https://genius.com/Keenv-saltimbanque-lyrics", "https://genius.com/Keenv-ma-vie-au-soleil-lyrics"]
def boucle_genius(urls):
    for url in urls:
        while True:
            page = requests.get(url).text
            soup = BeautifulSoup(page, "lxml")
            titre = soup.find(class_="SongHeader__Title-sc-1b7aqpg-7")
            artiste = soup.find(class_="SongHeader__Artist-sc-1b7aqpg-8")
            print("artiste : ", artiste, " titre : ", titre)
            if artiste != titre != None:
                emotions(url, titre.text, artiste.text)
                break

boucle_genius(urls)
