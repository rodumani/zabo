from zabo.apps.board.models import Article
from django.shortcuts import render
from zabo.apps.board.views import get_ctx

def view(request, name):
    articles = Article.objects.all().order_by('id')    #TODO gather only club(name) article
    template = 'club_info.html'
    page_template = 'board/view_page.html'
    if request.is_ajax():
        template = page_template

    return render(request, template, get_ctx(articles))
