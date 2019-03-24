from django.db import models
from django.contrib.auth.models import User
from datetime import timezone, datetime
from taggit.managers import TaggableManager 
from sorl.thumbnail import ImageField
from PIL import Image
from django.core import serializers
from django.template.defaultfilters import slugify


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Категории"

    cat = models.CharField(max_length=120, verbose_name="Категория")

    def __str__(self):
        return self.cat

class Img(models.Model):
    img = models.ImageField(verbose_name="Изображение")

    class Meta:
        verbose_name_plural = "Изображения"

def default_date():
    return datetime.now(tz=timezone.utc)

class ArticlesManager(models.Manager):
    def create_article(self, author, title, post, url, image_link):
        article = self.create(
            author=author,
            title=title,
            post=post,
            url=url,
            image_link=image_link,
            date=default_date())
        return article

    def update_article(self,author, title, post, url, image_link):
        article = self.update(
            author=author,
            title=title,
            post=post,
            url=url,
            image_link=image_link,
            date=default_date())
        return article


class Articles(models.Model):
    author = models.TextField(null=True, blank=True,verbose_name="Автор")
    title = models.CharField(max_length=120, verbose_name="Заголовок")
    post = models.TextField(verbose_name="Текст")
    url = models.TextField(null=True, blank=True, verbose_name="Урлы")
    tags = TaggableManager()
    image_link = models.TextField(
        null=True, blank=True, verbose_name="Cсылки на картинки")
    image = models.ImageField(
        blank=True,
        upload_to='images/',
        help_text='150x150px',
        verbose_name='Ссылка картинки')
    date = models.DateTimeField(verbose_name="Дата")
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Категория")
    objects = ArticlesManager()

    class Meta:
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title

    def __str__(self):
        return self.text
