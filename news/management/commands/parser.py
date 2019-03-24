from django.core.management.base import BaseCommand, CommandError
import requests
from bs4 import BeautifulSoup
from news.models import ArticlesManager, Articles


class Command(BaseCommand):
    help = 'Create new post'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        base_url = 'https://pg11.ru/articles?'
        page_part = "page="
        for i in range(1, 100):
            print(i, 'итерация')
            url = base_url + page_part + str(i)
            r = requests.get(url)
            html = r.text
            soup = BeautifulSoup(html, 'lxml')
            news = soup.find(
                'div', class_='article-list').find_all('h3', class_='article-list__item-title')
            for new in news:
                try:
                    title = new.find('a', class_='link_nodecor').text.strip()
                except:
                    title = ''

                try:
                    url = 'https://pg11.ru' + \
                        new.find('a', class_='link_nodecor').get('href')
                    post = requests.get(url)
                    soup = BeautifulSoup(post.text, 'lxml')
                    img = soup.find('div', class_='article__main-photo container-v').find(
                        'div', class_='article__main-photo-img')
                    div = str(soup.select('.article__main-photo-img')[0])
                    image_link = div.split('url(')[1][:-9]
                    articles = soup.find(
                        'div', class_='article__main-content').find_all('p')
                    sp = []
                    for article in articles:
                        p = article.get_text() + '<br>'
                        sp.append(p)
                    post = '    '.join(sp)
                    article = Articles.objects.create_article(
                        title, post, url, image_link)
                    print(
                        '==================================Созданная модель==============================', article)
                    print(title, 'Успешно сохранен')
                except:
                    url = ''
