from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Category, Products, Reviews, ProductImage
from accounts.models import UserAddress
from accounts.forms import Address


# Create your views here.
def home(request):
    reviews = Reviews.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, "index.html", context=context)

def productDetails(request, productDetailName):
    product_query = get_object_or_404(Products, slug=productDetailName)
    if product_query:
        product_detail = Products.objects.get(name=product_query)
        product_image = ProductImage.objects.filter(product=product_query)
        context = {
            'product_detail': product_detail,
            'product_image': product_image
        }
        return render(request, "product-details.html", context=context)

def productList(request, productListName):
    category = get_object_or_404(Category, name=productListName)
    if category:
        productList = Products.objects.filter(category=category)
        context = {
            'products': productList,
            'cat': productListName,
        }

        return render(request, "product-list.html", context=context)

@login_required(login_url='login')
def cart(request):
    user_address = Address(request.POST or None)
    if user_address.is_valid():
        print('save')
        user_address.save()
    else:
        user_address = Address()

    #address = UserAddress.objects.all()


    context = {
        'address': 'address',
        'address_form': user_address
    }
    return render(request, "cart.html", context=context)