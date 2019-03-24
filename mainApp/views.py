from django.shortcuts import render
from news.models import Articles


def index(request):
    articles = Articles.objects.order_by('-date')[0:5]
    return render(request, 'mainApp/homePage.html', {'articles': articles})


def contact(request):
    return render(
        request, 'mainApp/basic.html', {
            'content': [
                'Если у вас остались какие-либо вопросы, то вы можете написать по адресу:',
                '1234@mail.ru', 'web.example@gmail.com'
            ]
        })
