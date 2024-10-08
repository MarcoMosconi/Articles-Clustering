from bs4 import BeautifulSoup
import requests
import datetime

def scrape(article_content, all_articles):
    link = article_content.find("a", href=True)
    title = link.text
    soup = BeautifulSoup(requests.get(f"https://www.ansa.it{link['href']}").content, 'lxml')

    full_text = soup.find('div', class_='post-single-text rich-text news-txt')
    try:
        text = ' '.join([p.text for p in full_text.find_all('p') if 'Riproduzione riservata © Copyright ANSA' not in p.text])
        
        all_articles.append({
        'Publication': 'Ansa',
        'Date': datetime.date.today(),
        'Title': title,
        'Content': text
    })
    except AttributeError:
        pass

    return all_articles