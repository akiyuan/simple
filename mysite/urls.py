from django.contrib import admin, auth
from django.conf.urls import url, include
from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include('mainApp.urls')),
    url('news/', include('news.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^search/', include('search.urls'))]
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
