from django.shortcuts import render, HttpResponse
from datetime import datetime
from appPoemHub.models import Poems
# Create your views here.

def index(request):
    context = {
        'poems' : Poems.objects.all(),
    }

    return render(request, 'index.html', context)

def post(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        poem = request.POST.get('poem')
        title = request.POST.get('title')
        
        poems = Poems(name=name,poem=poem,date=datetime.today(),title=title)
        poems.save()
        
    return render(request,'post.html')

def signup(request):
   

    return render(request,'signup.html')
