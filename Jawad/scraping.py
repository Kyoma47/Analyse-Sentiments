import requests
from bs4 import BeautifulSoup
from bs4.element import Tag as tg
import pickle

def scraping_genius(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")

    div  = soup.find(class_="Lyrics__Container-sc-1ynbvzw-2 jgQsqn")
    if div!=None:
        paroles = [ ligne for ligne in div if type(ligne) != tg ]
    else: print("class!")#div  = soup.find(class_="song_body-lyrics")



    #text = [p.text for p in soup.find(class_="post-content").find_all('p')]
    #print(url)
    #return text

scraping_genius("https://genius.com/Keenv-les-mots-lyrics")
