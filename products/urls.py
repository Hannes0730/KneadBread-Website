from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home, productList, productDetails, cart
from django.views.static import serve

urlpatterns = [
    path('', home, name='home'),
    path('cart/', cart, name='cart'),
    path('products/<str:productListName>', productList, name='product-list'),
    path('product-detail/<str:productDetailName>', productDetails, name='product-detail', ),
    #path('products-detail/', productDetails, name='product-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)