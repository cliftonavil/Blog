
from django.contrib import admin
from django.urls import path,include
from .import views
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', article_view.articles_list, name='homepage'),
    path('about/', views.about),
    path('articles/', include('articles.urls')),
    path('accounts/',include('accounts.urls')),

]
urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
