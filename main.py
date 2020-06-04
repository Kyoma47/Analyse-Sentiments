import string
from collections import Counter
import matplotlib.pyplot as plt

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
    "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
    "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
    "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
    "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
    "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
    "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
    "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
    "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

def decouper(texte):
    minuscules = texte.lower()
    propre = minuscules.translate( str.maketrans('’',' ', string.punctuation + '…\t\n' ) )
    mots   = propre.split()
    usefull = [mot for mot in mots if mot not in stop_words and len(mot)>1]
    return usefull

def afficher(list_emotions, nom_image="graph.png" ):
    print(list_emotions)
    w = Counter(list_emotions)
    fig, axl = plt.subplots()
    plt.bar( w.keys(), w.values() )
    fig.autofmt_xdate()
    plt.savefig( nom_image )
    plt.show()
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





#main :
#nlt_fichier("read.txt")
nlt_tweets("corona virus", 500)
