from django.shortcuts import render

from django.views.generic import ListView
from django.db.models import Q
from news.models import Articles


class ArticleListView(ListView):
    model = Articles
    template_name = 'search/index.html'

    def get_queryset(self):
        # Получаем не отфильтрованный кверисет всех моделей
        queryset = super(ArticleListView, self).get_queryset()
        q = self.request.GET.get("q")
        if q:
            # Если 'q' в GET запросе, фильтруем кверисет по данным из 'q'
            return queryset.filter(Q(title__iexact=q) | Q(post__iexact=q))
        return queryset
