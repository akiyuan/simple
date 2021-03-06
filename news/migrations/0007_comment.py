# Generated by Django 2.0.7 on 2018-07-09 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0006_auto_20180615_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Комментарий')),
                ('pub_date', models.DateTimeField(verbose_name='Дата комментария')),
                ('article_id', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Articles')),
                ('author_id', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]
