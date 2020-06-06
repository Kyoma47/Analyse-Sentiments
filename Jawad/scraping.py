import requests
from bs4 import BeautifulSoup
from bs4.element import Tag as tg
import pickle
from main_nltk import decouper, afficher


def scraping_genius(url):
    print("while!")
    while True:
        page = requests.get(url).text
        soup = BeautifulSoup(page, "lxml")
        div = soup.find(class_="Lyrics__Container-sc-1ynbvzw-2 jgQsqn")
        if div!=None: return [str(ligne) for ligne in div if type(ligne) != tg]
        #div  = soup.find(class_="song_body-lyrics")

def mots_genius(url):
    mots = []
    for ligne in scraping_genius(url):
        mots += decouper(ligne)
    print(mots)
    return mots



url = "https://genius.com/Keenv-les-mots-lyrics"
liste = scraping_genius(url)

afficher(mots_genius(url))
