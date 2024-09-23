from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
from Corriere.scrape import scrape

def corriere_scraping():
    html_text = requests.get('https://www.corriere.it').text
    soup = BeautifulSoup(html_text, 'lxml')

    classes = ['bck-module bck-media-news el-show-desktop-only ']

    all_articles = []

    for class_ in classes:
        # articles = soup.find_all('div', class_=class_)
        # for article in articles:
        #     all_articles = scrape(article, all_articles)
        article = soup.find('div', class_=class_)
        all_articles = scrape(article, all_articles)


    df = pd.DataFrame(all_articles)
    df.to_csv(f'Articles\\Corriere-Articles\\corriere-articles-{datetime.date.today()}.csv')