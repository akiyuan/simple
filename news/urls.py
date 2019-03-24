from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from .models import Articles
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

from .views import new_post, ArticleListView, detail
urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='plist'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^post_new/$', views.new_post, name="new_post"),
    url(r'^update/(?P<pk>\d+)$', views.update_post, name='update'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='delete'),
    url(r'^tag/(?P<tag_id>[-\w]+)/$', views.tag_list, name='post_list_by_tag'),
]
