from django.urls import path, re_path
from .import views

app_name='artiles'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.articles_list,name="list"),
    # path('about/', views.about),
    path('art/', views.artii),
    re_path(r'^(?P<slug>[\w-]+)/$',views.articles_details,name="detail"),
]
