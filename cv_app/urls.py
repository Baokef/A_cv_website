from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('cv/', views.cv, name='cv'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('download_my_pdf/', views.download_pdf, name="download_pdf"),
]
