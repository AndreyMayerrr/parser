from bs4 import BeautifulSoup
import requests
import urllib3


def parse():
    filtered_news = []
    urllib3.disable_warnings()
    url = 'https://omgtu.ru/news/'
    page = requests.get(url, verify=False)
#    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")
#    print(soup)
    news = soup.find_all('h3', class_='news-card__title')
    for data in news:
        filtered_news.append(data.text)
    return filtered_news


def parse_write_to_file():
    with open('titles.txt', 'w') as f:
        for date in parse():
            f.write(date)
