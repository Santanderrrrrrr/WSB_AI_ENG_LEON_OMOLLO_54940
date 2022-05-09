from nltk.tokenize import LineTokenizer, SpaceTokenizer, word_tokenize, TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud


f = open("sample2.txt")
livTxt = f.read()

# lenizer = LineTokenizer()
# elTLiv = lenizer.tokenize(livTxt)
# print("Line tokenized")
# print(elTLiv)
#
# senizer =SpaceTokenizer()
# sLiv = senizer.tokenize(livTxt)
#
# print("Space tokenized")
# print(sLiv)
#
# wenizeLiv = word_tokenize(livTxt)
# print("Word tokenized")
# print(wenizeLiv)

twenizer = TweetTokenizer()
twenizeLiv = twenizer.tokenize(livTxt)
print("Tweet Tokenizer")
print(twenizeLiv)

##################################################################################

stop_words = set(stopwords.words("english"))
stopTwenizeLiv = []

for w in twenizeLiv:
    if w not in stop_words:
        stopTwenizeLiv.append(w)

print("tweet tokenized minus stop words")
print(stopTwenizeLiv)

################################################################################
lemmatizer = WordNetLemmatizer()

lemmaStopTwenizeLiv = []
toBeRemoved = ["'", '.', ',']

for w in stopTwenizeLiv:
    if w not in toBeRemoved:
        lemmaStopTwenizeLiv.append(lemmatizer.lemmatize(w))

print("tweet tokenized minus stop words then lemmatized")
print(lemmaStopTwenizeLiv)

################################################################################

data_set = lemmaStopTwenizeLiv
# split_data = data_set.split()
counter = Counter(data_set)
most_occur = dict(counter.most_common(10))

print("This is most occurring 10")
print(most_occur)




################################################################################

labels, values = zip(*most_occur.items())


indSort = np.argsort(values)[::-1]


labels = np.array(labels)[indSort]
values = np.array(values)[indSort]

indexes = np.arange(len(labels))

bar_width = 0

plt.bar(indexes, values)

# add labels
plt.title('10 most used words')
plt.xlabel('word')
plt.ylabel('frequency')
plt.xticks(indexes + bar_width, labels)
plt.show()

#################################################################################
wc = WordCloud(background_color="white",width=1000,height=1000, max_words=10,relative_scaling=0.5,normalize_plurals=False).generate_from_frequencies(most_occur)
plt.imshow(wc)
plt.show()

# reference: https://www.liverpoolecho.co.uk/news/liverpool-news/easy-point-finger-say-liverpool-23875841