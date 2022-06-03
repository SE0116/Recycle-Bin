from django.shortcuts import render
from .models import Feed


def home(request):
    feeds = Feed.objects.all()
    context = {
        'feeds': feeds,
    }
    return render(request, 'main/home.html', context)