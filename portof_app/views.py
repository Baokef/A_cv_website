from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    projet= {"prenom":"Oumar", "nom":"Bao","title":"portfolio"}
    return render(request,"cv_app/index.html",{"projet":projet})

def portfolio(request):
    projet= {"prenom":"Oumar", "nom":"Bao","title":"portfolio"}
    return render(request,"portof_app/portfolio.html",{"projet":projet})
