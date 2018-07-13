from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import Articles
from django.contrib.auth.decorators import login_required
from .import forms


def articles_list(request):
    # list all articles
    articles = Articles.objects.all().order_by('date')
    return render(request, 'articles/article_lists.html', {'articles': articles})


def artii(request):
    return render(request,'articles/artt.html')


def articles_details(request,slug):
    # detailed article view
    articles = Articles.objects.get(slug=slug)
    return render(request, 'articles/artile_deatil.html', {'articles': articles})


@login_required(login_url='/accounts/login/') #checking userloged in or not
def article_create(request):
    #creating articles
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            #save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            print('ccccc       Sucess ',form)
        return redirect('artiles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})