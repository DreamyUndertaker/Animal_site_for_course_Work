from . import views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django_email_verification import urls as email_urls 
from django.contrib.auth import views as authViews

urlpatterns = [
    path('login/', authViews.LoginView.as_view(template_name='home/signin.html'), name="login"),
    path('registration/', views.registration, name='registration'),
    path('email/', include(email_urls)),
    path('', views.home, name='home'),
    path('db/', include('db.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 