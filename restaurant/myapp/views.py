from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    cate=Category.objects.all()

    cateid=request.GET.get('category')
    if cateid:
        momo=Momo.objects.filter(category=cateid)
    else:
        momo=Momo.objects.all()

    context={
        'cate':cate,
        'momo':momo,
    }
    
    return render(request,'app/index.html',context)
def about(request):
    return render(request,'app/about.html')
def contact(request):
    return render(request,'app/contact.html')
def menu(request):
    return render(request,'app/menu.html')
def services(request):
    return render(request,'app/services.html')


