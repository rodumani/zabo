from django.db.models import Q
from django.shortcuts import render
from zabo.apps.account.models import UserProfile
from zabo.apps.board.models import Article
from zabo.apps.board.views import get_ctx

def view(request, name):
    club = UserProfile.objects.get(club_name_en=name)
    articles = Article.objects.filter(Q(writer__profile__club_name__iexact=name) | Q(writer__profile__club_name_en__iexact=name))
    template = 'club_info.html'
    page_template = 'board/view_page.html'
    if request.is_ajax():
        template = page_template

    ctx = get_ctx(articles)
    ctx['profile_image'] = club.profile_image
    ctx['club_name'] = club.club_name_en
    ctx['club_comment'] = club.club_comment

    return render(request, template, ctx)
