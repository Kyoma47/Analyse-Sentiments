from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

#Il est meilleure
phrase = "Il est meilleur"
print(phrase  +" : "+ str(TextBlob(phrase,pos_tagger=PatternTagger(),analyzer=PatternAnalyzer()).sentiment))

#Il n'est pas meilleure
phrase = "Il n'est pas meilleur"
print(phrase  +" : "+ str(TextBlob(phrase,pos_tagger=PatternTagger(),analyzer=PatternAnalyzer()).sentiment))

#Il est vraiment le meilleure
phrase = "Il est vraiment le meilleur"
print(phrase +" : "+ str(TextBlob(phrase,pos_tagger=PatternTagger(),analyzer=PatternAnalyzer()).sentiment))
