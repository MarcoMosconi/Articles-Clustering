from bs4 import BeautifulSoup
import requests

def scrape(article_content, all_articles, publication):
    link = article_content.find("a", href=True)
    title = link.text
    if not link['href'].startswith('http'):
        soup = BeautifulSoup(requests.get(f"https://www.{publication.lower()}.it{link['href']}").text, 'lxml')
    else:
        soup = BeautifulSoup(requests.get(link['href']).text, 'lxml')
        print(soup.prettify())
    if publication == 'Ansa':
        full_text = soup.find('div', class_='post-single-text rich-text news-txt')
    elif publication == 'ilPost':
        full_text = soup.find('div', class_='contenuto all mapp_render')
    text = ' '.join([p.text for p in full_text.find_all('p') if 'Riproduzione riservata © Copyright ANSA' not in p.text])

    all_articles.append({
        'Publication': publication,
        'Title': title,
        'Content': text
    })
    return all_articles