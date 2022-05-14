from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('membership/', views.membership, name='membership'),
]
