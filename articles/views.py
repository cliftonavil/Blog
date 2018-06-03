from django.shortcuts import render
from.models import Articles

# Create your views here.
def articles_list(request):
    articles=Articles.objects.all().order_by('date')
    print("@@@@@@@@@@@@", articles)
    return render(request,'articles/article_lists.html',{'articles':articles})

def artii(request):
    return render(request,'articles/artt.html')