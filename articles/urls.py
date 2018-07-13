from django.urls import path, re_path
from .import views


app_name = 'artiles'

urlpatterns = [
    path('', views.articles_list,name="list"),
    path('create/', views.article_create, name="create"),
    path('art/', views.artii),
    re_path(r'^(?P<slug>[\w-]+)/$',views.articles_details,name="detail"),
]
