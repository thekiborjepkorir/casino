from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html.')
def client(request):
    return render(request, 'client.html')
def contact(request):
    return render(request, 'contact.html')
def cycle(request):
    return render(request, 'cycle.html')
def electronic(request):
    return render(request, 'electronic.html.html')
def fashion(request):
    return render(request, 'fashion.html')
def game(request):
    return render(request, 'game.html')
def jewellery(request):
    return render(request, 'jewellery.html')
def news(request):
    return render(request, 'news.html')