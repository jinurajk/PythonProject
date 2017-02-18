from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob.sentiments import NaiveBayesAnalyzer

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass. able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists. fearful of
artificial intelligence run rampant.
'''

blob = TextBlob(text)

print(blob.tags)
print("\n",blob.noun_phrases)
for sentence in blob.sentences:
    print(sentence.sentiment.polarity)

b = TextBlob("I havv goood speling!")
print("Corrected spelling   :",b.correct())

#blob3 = TextBlob("What is your name")
#print(blob3.detect_language())
#print(blob3.translate(to='de'))

blob1 = TextBlob("I hate hate hate this library badly", analyzer=NaiveBayesAnalyzer())
print(blob1.sentiment)

blob2 = TextBlob("I love this library very much", analyzer=NaiveBayesAnalyzer())
print(blob2.sentiment)

print(blob.sentences)