from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('allproducts', views.allproducts, name="allproducts"),
    path('cart', views.cart, name="cart"),
    path('productinfo/<int:prodid>',
         views.productinfo, name="productinfo"),
    path('catProd/<int:catid>', views.catProd, name="catProd"),
    path('checkout', views.checkout, name="checkout"),
    path('search', views.search, name="search"),
    path('feedback', views.feedback, name="feedback"),
    path('order', views.order, name="order"),
]
