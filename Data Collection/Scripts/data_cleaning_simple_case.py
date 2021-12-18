# Run in python console
import csv

import gensim
import nltk;
from gensim.utils import simple_preprocess

nltk.download('stopwords')
import re
import numpy as np
import pandas as pd
from pprint import pprint
import spacy
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
# NLTK Stop words
from nltk.corpus import stopwords

stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use'])

listFile = ["commitmessagesf.csv"]
filePath = "/Users/mosesopenja/Documents/summer2020/Mouna/commit-message/v2/"
filePath2 = "/Users/mosesopenja/Documents/summer2020/Mouna/commit-message/v2/cleaned/"

# Import Dataset
for file_ in listFile:
    newFile = "" + file_.split(".")[0] + ""

    csv_build = filePath2 + newFile + ".csv"
    rows = ["System", "Text"]
    fileCSV = open(csv_build, 'w')
    writer = csv.writer(fileCSV)
    writer.writerow(rows)

    df = pd.read_csv('{}{}'.format(filePath, file_))
    #print(df.Text.unique())
    #df.head()

    # Convert to list
    data = df.message.values.tolist()
    paper_id = df.System.values.tolist()
    # CommentId = df.CommentId.values.tolist()
    # data = data+" "+Comments

    # Remove Emails
    data = [re.sub(r'\S*@\S*\s?', '', str(sent)) for sent in data]
    data = [re.sub('<pre>(.*?)</pre>', '', str(sent)) for sent in data]
    data = [re.sub('<code>(.*?)</code>', '', str(sent)) for sent in data]
    data = [re.sub('{code(.*?)}', '', str(sent)) for sent in data]
    # Remove new line characters
    data = [re.sub('<a(.*?)</a>', ' ', str(sent)) for sent in data]
    data = [re.sub('<p>', ' ', str(sent)) for sent in data]
    data = [re.sub('</p>', ' ', str(sent)) for sent in data]
    data = [re.sub('<li>', ' ', str(sent)) for sent in data]
    data = [re.sub('</li>', ' ', str(sent)) for sent in data]
    data = [re.sub('<ol>', ' ', str(sent)) for sent in data]
    data = [re.sub('</ol>', ' ', str(sent)) for sent in data]
    data = [re.sub('<em>', ' ', str(sent)) for sent in data]
    data = [re.sub('</em>', ' ', str(sent)) for sent in data]
    data = [re.sub('<blockquote>', ' ', str(sent)) for sent in data]
    data = [re.sub('</blockquote>', ' ', str(sent)) for sent in data]
    data = [re.sub('<h1>', ' ', str(sent)) for sent in data]
    data = [re.sub('</h1>', '', str(sent)) for sent in data]
    data = [re.sub('<h2>', '', str(sent)) for sent in data]
    data = [re.sub('</h2>', '', str(sent)) for sent in data]
    data = [re.sub('<h3>', '', str(sent)) for sent in data]
    data = [re.sub('</h3>', '', str(sent)) for sent in data]
    data = [re.sub('<h4>', '', str(sent)) for sent in data]
    data = [re.sub('</h4>', '', str(sent)) for sent in data]
    data = [re.sub('<h5>', '', str(sent)) for sent in data]
    data = [re.sub('</h5>', '', str(sent)) for sent in data]
    data = [re.sub('<h6>', '', str(sent)) for sent in data]
    data = [re.sub('</h6>', '', str(sent)) for sent in data]
    data = [re.sub('!', '', str(sent)) for sent in data]
    data = [re.sub(r'^https?:\/\/.*[\r\n]*', '', sent) for sent in data]
    data = [re.sub(r'^http?:\/\/.*[\r\n]*', '', sent) for sent in data]
    # Remove new line characters
    data = [re.sub('\s+', ' ', str(sent)) for sent in data]
    # Remove distracting single quotes
    data = [re.sub("\'", "", str(sent)) for sent in data]


    DataString = ""
    index = 0
    for data_ in data:
        data_ = re.sub(r'^https?:\/\/.*[\r\n]*', '', data_, flags=re.MULTILINE)
        data_ = re.sub(r'http\S+', '', data_)
        data_ = " ".join(filter(lambda x: x[0] != '#', data_.split()))
        data_ = " ".join(filter(lambda x: x[0] != '@', data_.split()))
        data_ = " ".join(filter(lambda x: x[0] != 'http', data_.split()))
        data_ = " ".join(filter(lambda x: x[0] != '-', data_.split()))
        data_ = " ".join(filter(lambda x: x[0] != '<', data_.split()))
        data_ = " ".join(filter(lambda x: x[0] != '=', data_.split()))

        # pprint(data[:1])
        data_words = data_
        bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100)  # higher threshold fewer phrases.
        trigram = gensim.models.Phrases(bigram[data_words], threshold=100)

        # Faster way to get a sentence clubbed as a trigram/bigram
        bigram_mod = gensim.models.phrases.Phraser(bigram)
        trigram_mod = gensim.models.phrases.Phraser(trigram)

        print(" \n----------\n")
        # pprint(data_words[:1])
        # DataString = DataString+" "+data_words+"\n"

        pprint("{} : {} ".format(index, data_words))
        rows = [paper_id[index], data_words]
        writer.writerow(rows)
        index += 1
