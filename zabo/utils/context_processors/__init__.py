from zabo.apps.board.models import CATEGORY_CHOICES

def layout_category(request):
    return {'choices': CATEGORY_CHOICES}
