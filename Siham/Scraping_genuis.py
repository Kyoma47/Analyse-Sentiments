# Web scraping, pickle imports
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

afficher(mots_genius("https://genius.com/Keenv-explique-moi-lyrics"))
