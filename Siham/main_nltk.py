import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from collections import Counter
import matplotlib.pyplot as plt

import os

def sentiment_analyse(texte):
    scores = SentimentIntensityAnalyzer().polarity_score(texte)
    negative, positive = score['neg'], score['pos']

def decouper(texte):
    Aremplacer = '’\n\t' + string.punctuation
    texte_propre = texte.lower().translate( str \
    .maketrans(Aremplacer, len(Aremplacer)*' ', '…0123456789'))
    mots = word_tokenize(texte_propre, "french")
    mots_utiles = [mot for mot in mots if mot not in stopwords.words("french")]
    return mots_utiles

def afficher(list_emotions, titre, artiste, nom_image="graph.png" ):
    w = Counter(list_emotions)
    if not os.path.exists(artiste):
        os.mkdir(artiste)
    fig, axl = plt.subplots()
    plt.bar( w.keys(), w.values() )
    fig.autofmt_xdate()
    plt.savefig(nomDossier + "\\" + titre)
    #plt.show()
    print(w)

def traitement(usefull):
    list_emotions = []
    with open("emotions.txt", 'r', encoding="utf-8") as fichier :
        for ligne in fichier :
            word, emotion = ligne.replace("\n", "").replace(",", "").replace("'", "").split(":")
            word, emotion = word.strip(), emotion.strip()
            if word in usefull :
                list_emotions.append(emotion)
    afficher(list_emotions)


def nlt_fichier(nom_fichier):
    texte = open(nom_fichier, encoding="utf-8").read()
    usefull = decouper(texte)
    traitement(usefull)


def get_tweets(requete, max=100, debut="2020-01-01", fin="2020-04-01"):
    import GetOldTweets3 as got
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(requete) \
        .setSince(debut) \
        .setUntil(fin) \
        .setMaxTweets(max)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [tweet.text for tweet in tweets]
    for i,text in enumerate(text_tweets):
        print( ("0" if i<10 else "")+ str(i), ":", text[:50])
    return text_tweets

def nlt_tweets(requete, max):
    final_words = []
    for tweet in get_tweets(requete, max):
        final_words += decouper(tweet)
    traitement(final_words)
