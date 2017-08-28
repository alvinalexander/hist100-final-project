import pandas as pd
import numpy as np

#Load the data files
df = pd.read_csv("../data//bbtop15-lyrics-master3.csv", index_col=0)


#Get list of dates.
dates = df['date'].tolist()



#create a list of year
years = [pd.Timestamp(date).year for date in dates]
#add year column to data
df['year'] =  years



df1 = df[['track', 'artist', 'artist_gender', 'date', 'year', 'lyrics' ]]


print(df1.head())

df1.to_csv(path_or_buf="../data/bbtop15-lyrics-master4.csv", index_label="track_id")
