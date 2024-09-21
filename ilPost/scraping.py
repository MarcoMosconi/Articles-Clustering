from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
from scrape import scrape

html_text = requests.get('https://www.ilpost.it/').text
soup = BeautifulSoup(html_text, 'lxml')


def ilpost_scraping():
    all_articles = []
    
    main_article = soup.find('div', class_='_article-content_fjfga_38')
    all_articles = scrape(main_article, all_articles, 'ilPost')

    df = pd.DataFrame(all_articles)
    df.to_csv(f'Articles\\ilPost-Articles\\ilpost-articles-{datetime.date.today()}.csv')
