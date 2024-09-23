from bs4 import BeautifulSoup
import requests
import datetime

def scrape(article_content, all_articles):
    link = article_content.find('a', href=True)
    title = ' '.join([link.text for link in article_content.find_all('a', href=True)])

    soup = BeautifulSoup(requests.get(link['href']).text, 'lxml')

    text = ' '.join([p.text for p in soup.find_all('p')])
    print(text)

    all_articles.append({
        'Publication': 'Corriere',
        'Date': datetime.date.today(),
        'Title': title,
        'Content': text
    })