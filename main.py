## Определяем список ключевых слов:
KEYWORDS = ['сети', 'парсер', 'телеграм', 'Python', 'SQL']

import requests
import bs4

if __name__ == '__main__':
    response = requests.get('https://habr.com/ru/articles/')
    soup = bs4.BeautifulSoup(response.text, features='lxml')

    articles = []
    articles_list = soup.findAll('article', class_='tm-articles-list__item')
    for article in articles_list:
        link = f"https://habr.com{article.find('a', class_='tm-title__link')['href']}"
        response = requests.get(link)
        soup = bs4.BeautifulSoup(response.text, features='lxml')
        title = soup.find('h1').text
        text = soup.find('div', id='post-content-body').text
        time = soup.find('time')['title']
        for word in KEYWORDS:
            if word in title or word in text:
                print(f'{time} - {title} - {link}')
                break
