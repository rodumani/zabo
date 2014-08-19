from zabo.apps.board.models import CATEGORY_CHOICES

def layout_category(request):
    choices = []
    urls = ['fresh', 'event']
    i = 0
    for x, y in CATEGORY_CHOICES:
        choices += [[urls[i], y]]
        i += 1
    return {'choices': choices}
