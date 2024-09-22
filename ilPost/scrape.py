from bs4 import BeautifulSoup
from selenium import webdriver
import datetime


def scrape(article_content, all_articles):
    driver = webdriver.Chrome()
    link = article_content.find("a", href=True)
    title = link.h2.text
    driver.get(link['href'])
    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    text = ' '.join([p.text for p in soup.find_all('p') if p.get('data-qr-index')])

    all_articles.append({
        'Publication': 'ilPost',
        'Date': datetime.date.today(),
        'Title': title,
        'Content': text
    })
    return all_articles