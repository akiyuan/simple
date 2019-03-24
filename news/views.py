from django.shortcuts import render
import json
from json import JSONEncoder
from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from .models import Articles, Category
from .forms import PostForm, EditPostForm
from django.utils import timezone
from django.views import View
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib import auth
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from taggit.models import Tag
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import FormView
from .mixins import AjaxFormMixin
from django.core import serializers
from django.views.decorators.http import require_POST


def detail(request, pk):
    articles = Articles.objects.get(id=pk)

    return render(request, 'news/post.html', {'articles': articles})


def delete(request, pk):
    article = Articles.objects.get(id=pk).delete()
    return redirect('plist')

class ArticleListView(ListView):
    model = Articles 
    template_name = 'news/posts.html'
    context_object_name = "post_list"
    ordering = ['-date']
    paginate_by = 10


def tag_list(request, tag_id=None):
    object_list = Articles.objects.all()
    tag = None

    if tag_id:
        tag = get_object_or_404(Tag, id=tag_id)
        object_list = object_list.filter(tags__in=[tag])

    return render(request, 'tags_sort/tags.html', {
        'tag': tag,
        'object_list': object_list
    })

def new_post(request):
    cat_list = Category.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.date = timezone.now()
            article.save()
            for tag in form.cleaned_data['tags']:
                article.tags.add(tag)
            return render(request, 'mainApp/homePage.html')
    else:
        form = PostForm()
    return render(request, 'add_news/add_post_new.html', {
        'form': form,
        'cat_list': cat_list
    })

def update_post(request, pk):
    cat_list = Category.objects.all()
    if request.method == "POST":
        id = request.POST.get('id', None)
        article = get_object_or_404(Articles, id=pk)
        form = EditPostForm(request.POST, request.FILES)
        article.title = request.POST.get('title')
        article.post = request.POST.get('post')
        article.tags = request.POST.get('tags')
        article.save()
        return redirect('plist')
    else:
        form = EditPostForm()
    return render(request, 'edit_post/edit_post_new.html', {
        'form': form,
        'cat_list': cat_list
    })
