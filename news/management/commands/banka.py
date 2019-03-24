from django.core.management.base import BaseCommand, CommandError
import requests
from bs4 import BeautifulSoup
from news.models import ArticlesManager, Articles


class Command(BaseCommand):
    help = 'Create new post'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        base_url = 'https://www.bnkomi.ru/data/news'
        page_part = "/go/"
        for i in range(1, 100):
            print(i, 'итерация')
            url = base_url + page_part + str(i)
            r = requests.get(url)
            html = r.text
            soup = BeautifulSoup(html, 'lxml')
            news = soup.find('div', class_='b-news-list')
            for new in news:
                try:
                    title = new.find('h2', class_='title').find('a').get_text()
                except:
                    title = ''
                try:
                    url = 'https://www.bnkomi.ru' + \
                        new.find('h2', class_='title').find('a').get('href')
                    post = requests.get(url)
                    soup = BeautifulSoup(post.text, 'lxml')
                    articles = soup.find(
                        'div', class_='cnt daGallery').find_all('p')
                    pa = []
                    for article in articles:
                        p = article.get_text() + '<br>'
                        pa.append(p)
                    post = ' '.join(pa)
                    article = Articles.objects.create_article(title, post, url)
                    print(
                        '=======================статья======================', article)

                except:
                    url = ''
