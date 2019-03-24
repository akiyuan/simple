from django.conf.urls import url

from . import views
from .views import ArticleListView

urlpatterns = [
    url(r'^article_search/', ArticleListView.as_view(), name='article_search'),
]
