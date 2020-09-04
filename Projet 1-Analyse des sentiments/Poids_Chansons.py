import string
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString
import os
from pathlib import Path
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

mots_positifs = open("positif_words.txt", encoding='utf-8').read().lower() \
.translate(str.maketrans('', '', string.punctuation + '\t')) \
.split()

mots_negatifs = open("negatif_words.txt", encoding='utf-8').read().lower() \
.translate(str.maketrans('', '', string.punctuation + '\t')) \
.split()


def rechercher_page(url):
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


def sauvegarder_donnees(url):
    soup = rechercher_page(url)
    liste_paroles = recuperer_paroles(soup)

    titre   = soup.find(class_="SongHeader__Title-sc-1b7aqpg-7").text.strip()
    artiste = soup.find(class_="SongHeader__Artist-sc-1b7aqpg-8").text.strip()

    if not os.path.exists("Chansons/"+artiste): os.mkdir("Chansons/"+artiste)

    with open( "Chansons/"+artiste+"/"+titre+".txt", 'w+', encoding="utf-8") as fichier:
        for ligne in liste_paroles : fichier.write(ligne+"\n")
    print( artiste+"/"+titre+".txt créé.")
    return artiste+"/"+titre


#Cleaning Data
def nettoyer_donnees(nomFichier) :
    texte = open("Chansons/"+nomFichier+".txt", encoding='utf-8').read().lower()
    texte_propre = texte.translate( str\
    .maketrans('’\n\t-',4*' ', string.punctuation + '…0123456789'+"«»"))
    mots = word_tokenize(texte_propre, "french")
    mots_utiles = [mot for mot in mots if mot not in stopwords.words("french")]
    return mots_utiles


def calculer_poids(nomFichier):
    poids = 0
    liste_mots = nettoyer_donnees(nomFichier)
    for mot in liste_mots:
        if mot in mots_positifs:
            poids += 1
        elif mot in mots_negatifs:
            poids -= 1

    if poids > 0:
        print(nomFichier+" est positif : Poids("+str(poids)+")\n")
    else:
        print(nomFichier+" est négatif : Poids("+str(poids)+")\n")


def traiter_target(separement=True):
    with open("targets.txt", "r", encoding="utf-8") as file:
        for lien in file:
            if len(lien)>1:
                target = sauvegarder_donnees(lien.strip())
                calculer_poids(target)

traiter_target()
