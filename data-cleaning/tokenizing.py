import pandas
import nltk
import string
import matplotlib.pyplot as plt
import re
import string
from functools import reduce
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
porter = nltk.PorterStemmer()
snowball = SnowballStemmer("english")



table = str.maketrans('', '', string.punctuation)

def clean_token(token):
    return token.translate(table)


#read in our data
df = pandas.read_csv("../data/bbtop15-lyrics-master4.csv", index_col=0)

#Drop na
df = df.dropna(subset=["lyrics"])


# Remove all text that is in square brackets
df['lyrics_clean'] = df['lyrics'].apply(lambda x: re.sub(r'\[.*\]', '', x))

#removing apostrophy
df['lyrics_clean'] = df['lyrics_clean'].apply(lambda x: x.replace("'", ''))


##### TOKENIZING ####
#Split on white space, lower case
#tokens_list = [song.split() for song in lyrics]
df['tokens'] = df['lyrics_clean'].apply(lambda x: x.split())

#print(reduce((lambda x, y: x + y), [len(tokens) for tokens in tokens_list]))

print(type(df['tokens'][0]))
##### NORMALIZING ####

##Lowercase
#token_list_lower = [[token.lower() for token in group] for group in tokens_list]
df['tokens_lower'] = df['tokens'].apply(lambda x: [token.lower() for token in x])

#Remove punctuation
#token_list_lower = [[clean_token(token) for token in group] for group in token_list_lower]
df['tokens_lower_clean'] = df['tokens_lower'].apply(lambda x: [token for token in x if (token not in list(string.punctuation)) and (re.match(r"['`]['`]", token) == None)])
df['tokens_lower_clean'] = df['tokens_lower_clean'].apply(lambda x: [clean_token(token) for token in x])


#Drop empty strings
#token_list_lower = [[token for token in group if token] for group in token_list_lower]
df['tokens_lower_clean'] = df['tokens_lower_clean'].apply(lambda x: [token for token in x if token])
#print(reduce((lambda x, y: x + y), [len(tokens) for tokens in token_list_lower]))

##### Excluding classes of words ####
#Drop digits
#token_list_lower = [[token for token in group if not token.isdigit()] for group in token_list_lower]
df['tokens_lower_clean_stopfree'] = df['tokens_lower_clean'].apply(lambda x: [token for token in x if not token.isdigit()])


#Remove stop-words
#token_list_lower_stopfree = [[token for token in group if token not in stopwords.words('english')] for group in token_list_lower]
#print(token_list_lower_stopfree[0])
#print(reduce((lambda x, y: x + y), [len(tokens) for tokens in token_list_lower_stopfree]))
df['tokens_lower_clean_stopfree'] = df['tokens_lower_clean_stopfree'].apply(lambda x: [token for token in x if token not in stopwords.words('english')])
#print(df['tokens_lower_clean_stopfree'][0])

####Stemming####
df['tokens_lower_clean_stopfree_stem'] = df['tokens_lower_clean_stopfree'].apply(lambda x: [snowball.stem(token) for token in x ])
#tokens_lower_stopfree_stemmed = [[porter.stem(t) for t in group] for group in token_list_lower_stopfree]

print(type(df['tokens_lower_clean_stopfree_stem'][0]))

df.to_csv(path_or_buf="../data/bbtop15-lyrics-tokenized.csv", index_label="track_id")