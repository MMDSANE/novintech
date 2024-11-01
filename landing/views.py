from django.shortcuts import render

def landing(request):
    return render(request, "index.html")


def c404(request):
    return render(request, '404.html', status=404)