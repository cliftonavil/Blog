from django.http import HttpResponse
from django.shortcuts import render
from.models import Articles

# Create your views here.
def articles_list(request):
    articles=Articles.objects.all().order_by('date')
    print("@@@@@@@@@@@@", articles)
    return render(request,'articles/article_lists.html',{'articles':articles})

def artii(request):
    return render(request,'articles/artt.html')

def articles_details(request,slug):
    articles=Articles.objects.get(slug=slug)
    return render(request,'articles/artile_deatil.html',{'articles':articles})