import pandas as pd
import numpy as np
import string
import re

#cleaning artist name
punctuation = string.punctuation
punctuation = punctuation + '’'

table = str.maketrans('', '', punctuation)

def clean_artist_name(artist):
    return artist.translate(table).lower().replace(' ', '')

def is_correct_artist(artist1, artist2):
    artist = re.search(artist2, artist1)
    if artist:
        return True
    return False


#Load the data files
df = pd.read_csv("../data//bbtop15-lyrics-master2.csv", index_col=0)

artist_list = df["artist"].tolist()

artist_list_clean = [clean_artist_name(artist) for artist in artist_list]

#Create list of female rappers
female_rappers_string = open('../data/female-rappers.txt', encoding='utf-8').read()
female_rappers = female_rappers_string.split("\n")
female_rappers_clean = [clean_artist_name(artist) for artist in female_rappers]




gender_list = []

for artist in artist_list_clean:

    artist_gender = None

    for female in female_rappers_clean:

        if is_correct_artist(artist, female) and female !="la":

            artist_gender = "Female"

    if artist_gender:

        gender_list.append(artist_gender)
    else:
        gender_list.append("Male")
male_rappers = [gender for gender in gender_list if gender == "Male"]

fem_rappers = [gender for gender in gender_list if gender == "Female"]


df["artist_gender"] = gender_list

girls = df[df["artist_gender"] == "Female"]

print(girls)

df.to_csv(path_or_buf="../data/bbtop15-lyrics-master3.csv", index_label="track_id")
#get a string of all the artist

#creta and empty arryay. loop over each artist in the csv. if a artist from the female rapper list apear in the artist string, then add female to the list, else add male.