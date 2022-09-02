# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 12:38:41 2022

@author: aacac
"""
import pandas as pd
import wget
import gzip
import shutil

path = r'C:\projeto-ETL\\'

#baixando o arquivo tsv do imdb
wget.download('https://datasets.imdbws.com/title.basics.tsv.gz')

#descompactanto o arquivo tsv do imdb
with gzip.open(path+'title.basics.tsv.gz', 'rb') as entrada:
    with open(path+'title_basics.tsv', 'wb') as saida:
        shutil.copyfileobj(entrada, saida)

#lendo o tsv do imdb
df_basics = pd.read_csv(path+"title_basics.tsv", sep="\t",low_memory=False, na_values=["\\N","nan"])

#lendo o output do web scraping
ws = pd.read_csv(path+'web_scraping_imdb.csv', sep=';')

#merge
df = pd.merge(ws, df_basics, right_on='primaryTitle', left_on='Title')

#Filtrando os 250 filmes
df['diff'] = df['Year'] - df['startYear']

#top0 
top0 = df.loc[df['diff']==0]
top0 = top0.loc[top0['titleType']=='movie']
top0 = top0.drop_duplicates()

#top1
top1 = pd.merge(ws, top0, on='Title', how='left')
top1 = top1[top1['tconst'].isnull()]
top1 = top1[['Title', 'Year_x', 'Rank_x', 'Rating_x']]
top1 = top1.rename(columns={'Year_x':'Year', 'Rank_x':'Rank', 'Rating_x':'Rating'})


#concatenando
df_final = pd.concat([top0, top1])
df_final = df_final.fillna('N/A')
df_final = df_final.drop_duplicates(subset='Title')

#tratamentos finais
df_final = df_final.drop(columns=['endYear', 'diff'])
df_final = df_final.sort_values(by=['Rank'])

#exportando
df_final.to_csv(path+'imdb_top250.csv', sep=';', index=False, encoding='utf-8')






