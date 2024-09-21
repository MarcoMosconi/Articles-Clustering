from bs4 import BeautifulSoup
import requests
import pandas as pd
from scrape import scrape

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
                all_articles = scrape(article, all_articles)
    elif column == 'column-big no-margin':
        col_articles = col.find('div', class_='articles-list')
        articles = col_articles.find_all('div', 'article-content')
        for article in articles:
            if not article.svg:
                all_articles = scrape(article, all_articles)
    else:            
        articles = col.find_all('div', 'article-content')
        for article in articles:
            all_articles = scrape(article, all_articles)

# main_column = soup.find('div', class_='main-column')
# main_articles = main_column.find_all('div', 'article-content')
# for main_article_content in main_articles:
#     all_articles = scrape(main_article_content, all_articles)

# small_column = soup.find('div', class_='column-small')
# small_col_articles = small_column.find('div', class_='articles-list')
# small_articles = small_col_articles.find_all('div', 'article-content')
# for small_article_content in small_articles:
#     if 'English' not in small_article_content.p.text:
#         all_articles = scrape(small_article_content, all_articles)

# right_column = soup.find('div', class_='column-big no-margin')
# right_col_articles = right_column.find('div', 'articles-list')
# right_articles = right_col_articles.find_all('div', 'article-content')
# for right_article_content in right_articles:
#     if not right_article_content.svg:
#         all_articles = scrape(right_article_content, all_articles)

# left_column = soup.find('div', class_='column big left')
# left_articles = left_column.find_all('div', 'article-content')
# for left_article_content in left_articles:
#     all_articles = scrape(left_article_content, all_articles)

# middle_column = soup.find('div', class_='column middle')
# middle_articles = middle_column.find_all('div', 'article-content')
# for middle_article_content in middle_articles:
#     all_articles = scrape(middle_article_content, all_articles)

print(all_articles)

df = pd.DataFrame(all_articles)

df.to_csv('articles.csv')