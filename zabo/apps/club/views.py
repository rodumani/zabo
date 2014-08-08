from zabo.apps.board.models import Article
from django.shortcuts import render

def view(request, name):
    articles = Article.objects.all().order_by('id')    #temporary
    no_of_articles = Article.objects.count()           #temporary
    return render(request, 'club_info.html', {'chosen':articles,'no_of_articles':no_of_articles})
