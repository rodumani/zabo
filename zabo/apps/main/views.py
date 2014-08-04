from django.shortcuts import redirect, render

def main(request):
#    return render(request, 'layout.html', {})
    return redirect('/main/')
