import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


response = requests.get("https://www.cambridge.org/core/journals/journal-of-child-language/most-cited?pageNum=2&searchWithinIds=C644EF3F5D5C03A3B735A52482A810B8&productType=JOURNAL_ARTICLE&pageSize=20&filters%5BisCitedByMin%5D=0&template=cambridge-core%2Fjournal%2Farticle-listings%2Flistings-wrapper&displayNasaAds=false&showCitationNumbers=true&suppressArticleTypeGrouping=true&sort=platformMetadata.citationCount.crossRef%3Adesc")
content = response.content

parser = BeautifulSoup(content, 'html.parser')

body = parser.body
print(body)



t = []
d = []
c = []
for i in range(1, 25):
    response = requests.get(
        "https://www.cambridge.org/core/journals/journal-of-child-language/most-cited?pageNum={}&searchWithinIds=C644EF3F5D5C03A3B735A52482A810B8&productType=JOURNAL_ARTICLE&pageSize=20&filters%5BisCitedByMin%5D=0&template=cambridge-core%2Fjournal%2Farticle-listings%2Flistings-wrapper&displayNasaAds=false&showCitationNumbers=true&suppressArticleTypeGrouping=true&sort=platformMetadata.citationCount.crossRef%3Adesc".format(i))
    content = response.content
    parser = BeautifulSoup(content, 'html.parser')
    citeNums = parser.find_all("span", class_="number")
    titles = parser.find_all("li", class_="title")
    dates = parser.find_all("span", class_="date")
    count = 0


    for title in titles:
        d.append(dates[count].text)
        c.append(citeNums[count].text)
        t.append(title.text.replace('\n','').replace('*','').replace(':','').lower())
        count+=1

frame = pd.DataFrame({'date': d,
                      'citedCount': c}, index = t)
frame.to_csv('metadata.csv')


