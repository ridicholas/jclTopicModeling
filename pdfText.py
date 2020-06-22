import PyPDF2, os
import numpy as np
import pandas as pd
import requests
from tika import parser
import csv
from bs4 import BeautifulSoup


directory = 'articles'

articles = pd.Series()
fails = pd.Series()
count = 0





for file in os.scandir(directory):


    raw=parser.from_file(file.path,xmlContent=True)['content']
    data = BeautifulSoup(raw)
    message = data.findAll(class_='page')  # for first page

    title = file.name.replace('.pdf','').replace('_',' ').lower()
    text = ''
    p = 1

    for page in message:
        try:
            text += page.text
            text += '/pageBreak'
            print('Appending {}: Page {}'.format(title, p))
        except:
            print('Failed {}: {}'.format(title, p))
            fails[title]=p

        p+=1

    articles[title] = text.replace(',','')
    count+=1

frame = pd.DataFrame(articles,columns=['text'])
frame.to_pickle('articles.pkl')
frame.head(10)



