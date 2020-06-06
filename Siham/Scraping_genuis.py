# Web scraping, pickle imports
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag as tg
import pickle
from main_nltk import decouper


def scraping_genuis(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    div = soup.find(class_="Lyrics__Container-sc-1ynbvzw-2 jgQsqn")
    if div != None:
        return [ligne for ligne in div if type(ligne) != tg]

list = scraping_genuis("https://genius.com/Keenv-les-mots-lyrics")
print(decouper("bonjour tout,; le Monde."))
