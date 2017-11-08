import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_list =[]
for line in open('ELECTION_ID','r'):
    #print(line.strip('\n').split('\t')[1])
    year = line.strip('\n').split('\t')[0]
    filename = year+'.csv'
    header = pd.read_csv(filename, nrows=1).dropna(axis=1)
    header_dict = header.iloc[0].to_dict()
    df = pd.read_csv(filename, index_col = 0,thousands = ",", skiprows = [1],nrows=4).dropna(axis=1)
    df.rename(inplace = True , columns=header_dict)
    df["Year"] = year
    share_list = []
    for index in range(0,len(df)):
        share = df['Republican'][index] /df['Total Votes Cast'][index]
        share_list.append(share)
    col_share = pd.Series(data=share_list,index=df.index)
    after_df = df[['Democratic', 'Republican', 'Total Votes Cast', 'Year']].copy()
    after_df['Republican Share']  = col_share
    df_list.append(after_df)
    #df.to_csv("test.csv")
#'''
res_df = pd.concat(df_list)

for item in  res_df.groupby('County/City'):
    item[1].sort_values(['Year']).plot(x='Year',y='Republican Share',legend=False)
    plt.title(item[0])
    plt.show()
    #print(item[1])


