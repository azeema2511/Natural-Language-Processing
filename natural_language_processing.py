!pip inpip instal# Natural Language Processing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud

# Importing the dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

#Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)



from collections import Counter

word_counter = Counter(corpus)
print(word_counter)
#text = "keys coding competetive development Python webscraping automation getsetpython projects cool awesome blockchain data machinelearning  regex loops datascience opencv ML list dictionary analysis sentiment variable set counter enumerate try except if-else for function class object instance GUI encryption security"

cloud = WordCloud(background_color="white").generate(str(corpus))

plt.imshow(cloud)
plt.axis('off')
plt.show()

dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)