from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    # path("portfolio/", portfolio),
    
    path('portfolio/', views.portfolio, name='portfolio'),
]