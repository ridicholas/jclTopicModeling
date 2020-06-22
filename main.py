import pandas as pd
import numpy as np
import re



def main():
    df = pd.read_pickle('articles.pkl')
    df['extract'] = df.text.str.extract(r'(Received .+\))')
    df['extract'] = df['extract'].apply(lambda x: fix(str(x)))

    df['date'] = df['extract'].str.extract(r'(\w+ \d{4})')
    nanBools = df.date.isnull()
    df['year'] = df.date.str.extract(r'(\d{4})')
    nanRepls = pd.Series(df.loc[nanBools,'text'].str.extract(r'(\d{4})')[0])
    nanRepls.name='year'
    df.update(nanRepls)

    df['text'] = df['text'].apply(lambda x: ''.join(["" if ord(i) < 32 or ord(i) > 126 else i for i in x]))
    df = df.replace('\n', '')
    df = df.replace('\r', '')
    df = df.replace(',', '')
    df.year = df.year.replace('1017','0')
    df.year = df.year = df.year.fillna(0)
    df.year = df.year.astype(int)
    df = df.drop('extract', axis=1)
    print(np.sort(df.year.unique()))
    df.to_pickle('allArticles.pkl')




def fix(s):
    new = ''
    for c in s:
        if ord(c)>=63280:
            c = chr(ord(c)-63232)
        new += c
    return new

if __name__ == '__main__':
    main()