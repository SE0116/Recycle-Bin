from django.shortcuts import render
from .models import Feed


def index(request):
    feeds = Feed.objects.all()
    context = {
        'feeds': feeds,
    }
    return render(request, 'articles/index.html', context)