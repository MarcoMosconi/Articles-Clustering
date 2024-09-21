from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
from scrape import scrape

def ansa_scraping():
    html_text = requests.get('https://www.ansa.it').text
    soup = BeautifulSoup(html_text, 'lxml')

    columns = ['main-column',
           'column-small',
           'column-big no-margin',
           'column big left',
           'column middle']

    all_articles = []

    for column in columns:
        col = soup.find('div', class_=column)
        if column == 'column-small':
            col_articles = col.find('div', class_='articles-list')
            articles = col_articles.find_all('div', 'article-content')
            for article in articles:
                if 'English' not in article.p.text:
                    all_articles = scrape(article, all_articles, 'Ansa')
        elif column == 'column-big no-margin':
            col_articles = col.find('div', class_='articles-list')
            articles = col_articles.find_all('div', 'article-content')
            for article in articles:
                if not article.svg:
                    all_articles = scrape(article, all_articles, 'Ansa')
        else:            
            articles = col.find_all('div', 'article-content')
            for article in articles:
                all_articles = scrape(article, all_articles, 'Ansa')

        df = pd.DataFrame(all_articles)

        df.to_csv(f'Articles\\Ansa-Articles\\ansa-articles-{datetime.date.today()}.csv')