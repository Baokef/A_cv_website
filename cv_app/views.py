from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    projet= {"prenom":"Oumar", "nom":"Bao","title":"Site Web CV"}
    return render(request,"cv_app/index.html",{"projet":projet})

def cv(request):
    projet= {"prenom":"Oumar", "nom":"Bao","title":"Site Web CV"}
    return render(request,"cv_app/cv.html",{"projet":projet})
def portfolio(request):
    projet= {"prenom":"Oumar", "nom":"Bao","title":"Site Web CV"}
    return render(request,"cv_app/portfolio2.html",{"projet":projet})
def download_pdf(request):
    projet= {"prenom":"Oumar", "nom":"Bao","title":"Site Web CV"}
    return render(request,"cv_app/download_pdf.html",{"projet":projet})