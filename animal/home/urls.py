from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.registration,name="reg"),
    path('login/', authViews.LoginView.as_view(template_name='home/signin.html'), name="login"),
    path('exit/', authViews.LogoutView.as_view(template_name='web/index.html'), name="exit"),
    path('home', views.home, name='home'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 