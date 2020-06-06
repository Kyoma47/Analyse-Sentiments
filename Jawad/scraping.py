import requests
from bs4 import BeautifulSoup
from bs4.element import Tag as tg
import pickle



def scraping_genius(url):
    print("while!")
    while True:
        page = requests.get(url).text
        soup = BeautifulSoup(page, "lxml")
        div = soup.find(class_="Lyrics__Container-sc-1ynbvzw-2 jgQsqn")
        if div!=None: return [ligne for ligne in div if type(ligne) != tg]
        #div  = soup.find(class_="song_body-lyrics")

liste = scraping_genius("https://genius.com/Keenv-les-mots-lyrics")
