from django.urls import path,include
from cloudstackApp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
