from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apis import views
from rest_framework_simplejwt import views as jwt_views

from apis.views import *
   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view()),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view()),
    path('', views.home),
    path('singup', UserRegistrationView.as_view()),# create manager
    path('login', UserLoginView.as_view()),
    path('logout', UserLogOutView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)