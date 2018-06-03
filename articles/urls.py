from django.urls import path
from .import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('list/', views.articles_list),
    # path('about/', views.about),
    path('art/', views.artii),
]
