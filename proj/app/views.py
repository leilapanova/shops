from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(requests):
    products = Products.objects.all()
    return render(requests, 'app/index.html', context={'products': products})


def create(request):
    if request.method == "POST":
        form = AddProduct(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            url = form.cleaned_data['url']
            price = form.cleaned_data['price']
            Products.objects.create(title=title, content=content, url=url, price=price)

            return redirect('home')
        else:
            form = AddProduct()
            return render(request, 'app/create.html', context={'form': form})
    else:
        form = AddProduct()
        return render(request, 'app/create.html', context={'form': form})


def delete(request, id):
    try:
        products = Products.objects.get(id=id)
        products.delete()
        return redirect('home')
    except:
        return redirect('home')


def product(request, id):
    try:
        product = Products.objects.get(id=id)
        return render(request, 'app/product.html', context={'product': product})
    except:
        return redirect('home')


def update(request, id):
    try:
        product = Products.objects.get(id=id)
        
        if request.method == "POST":
            product.title = request.POST.get('title')
            product.content = request.POST.get('content')
            product.url = request.POST.get('url')
            product.price = request.POST.get('price')

            product.save()
            return redirect('home')
        else:
            return render(request, 'app/update.html', context={'product': product})
    except:
        return redirect('home')
