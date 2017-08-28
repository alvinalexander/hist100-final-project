import pandas as pd
import numpy as np

#Load the data files
df1 = pd.read_csv("../data//bbtop15-master.csv", index_col=0)
del df1['Unnamed: 0.1']
del df1['position']

df2 = pd.read_csv("../data/bbtop15-lyrics-master.csv", index_col=1)
#replace Nan witn numpy nan value

df1['lyrics'].replace(to_replace='Nan',
    value= np.nan,
    inplace=True
)

#Combine the two data frames
#result = df_master.combine_first(df_missing_515).sort_values(by="Unnamed: 0")
#result = pd.merge(df_master, df_missing_515, left_on="track", right_on="track", how="outer")

#result = result[['artist_x', 'track', 'date_x', 'lyrics_y']]

#new_columns = ['artist', 'track', 'date', 'lyrics']

#result.columns = new_columns


lyrics = df2['lyrics'].tolist()

df1['lyrics'] = lyrics
#Check result
print(df1.describe(include="all"))

print(df1.head())
missing = df1[df1['lyrics'].isnull()]


<<<<<<< HEAD
#Combine the two data frames
<<<<<<< HEAD
result = df_master.combine_first(df_missing_515).sort_values(by= 'Unnamed: 0')


#Create csv file
result.set_index('Unnamed: 0', inplace=True)

result.to_csv(path_or_buf="../data/bbtop15-lyrics-master.csv", index_label="track_id")
=======
result = df_master.combine_first(df_missing_515).sort_values(by="Unnamed: 0")
=======
>>>>>>> merge-csv


#Create csv file
#print(result.head())
<<<<<<< HEAD
result.to_csv(path_or_buf="../data/bbtop15-lyrics-master.csv", index_label="track")
>>>>>>> merge-csv
=======
df1.to_csv(path_or_buf="../data/bbtop15-lyrics-master2.csv", index_label="track_id")
>>>>>>> merge-csv
