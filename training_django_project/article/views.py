from django.shortcuts import render


ARTICLES = ['Article1', 'Article2', 'Article3']


def index(request):
    return render(request, 'articles/index.html', context={
        'articles': ARTICLES,
    })
