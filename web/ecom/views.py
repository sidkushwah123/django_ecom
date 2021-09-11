 from django.shortcuts import render,HttpResponse
from .models import product ,contact as msg
from math import ceil



def index(request):
    # products = product.objects.all()
    # n = len(products)
    # no_of_slides = n//4 + ceil((n/4) - (n//4))
    # params ={"product":products,"no_of_slides":no_of_slides,'range':range(1,no_of_slides)}
    # allprod = [[ products,range(1,no_of_slides),no_of_slides],
    #             [products,range(1,no_of_slides),no_of_slides]]

    allprod = []
    catprod = product.objects.values("category","id")
    cats = {item["category"] for item in catprod}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n = len(prod)
        no_of_slides = n//4 + ceil((n/4) - (n//4))
        allprod.append([prod,range(1,no_of_slides),no_of_slides])
        

    
    params = {"allprod":allprod} 
    return render(request,"ecom/index.html",params)

def about(request):
    return render(request,"ecom/about.html")

def contact(request):
    if request.method=='POST':
        name=request.POST.get('Name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        data=msg(name=name,email=email,phone=phone,desc=desc)
        data.save()
    return render(request,"ecom/contact.html")

def tracker(request):
    return render(request,"ecom/tracker.html")

def search(request):
    return HttpResponse("about search")

def productview(request, id):
    #fetch the product by it id

    products=product.objects.filter(id=id)
    return render(request,"ecom/productview.html",{"product":products[0]})

def cheakout(request):
    return HttpResponse("kalo cheak out nhai ho payego lapad pad jayego ")
# Create your views here.
