# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 09:57:36 2022

@author: aacac
"""

from bs4 import BeautifulSoup
import requests 
import pandas as pd

path = r'C:\Users\aacac\OneDrive\Área de Trabalho\Ciência de Dados - Uni7\ETL\Datasets\\'

#alterando a linguagem 
headers = {'Accept-Language': 'en-US,en;q=0.5'}

#Acessando o site do IMDB
source = requests.get('    ', headers=headers)

#Verificando status de erro  
source.raise_for_status()

#Retornando o html ddo site 
soup = BeautifulSoup(source.text, 'html.parser')
movies = soup.find('tbody', class_= 'lister-list').find_all('tr')

# iterando por cada tag 

lista_name = []
lista_year = []
lista_rank = []
lista_rating = []

for movie in movies:
  
    name = movie.find('td', class_='titleColumn').a.text
    lista_name.append(name)
    rank = movie.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
    lista_rank.append(rank)
    year = movie.find('td', class_='titleColumn').span.text.strip('()')
    lista_year.append(year)
    rating = movie.find('td', class_ ="ratingColumn imdbRating").strong.text
    lista_rating.append(rating)
    print(name, rank, year, rating)

#criando o dataframe
df = pd.DataFrame(list(zip(lista_name,lista_year, lista_rank, lista_rating)), columns = ['Title','Year','Rank', 'Rating'])
df.drop_duplicates(inplace=True)

#to_csv
df.to_csv(path+'web_scraping_imdb.csv', sep=';', encoding='utf-8', index=False)