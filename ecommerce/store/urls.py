from django.urls import path
from . import views

# give route to make connections between the pages
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products_page, name='products_page'),
    path('get-products/', views.get_products, name='get_products'),
    path('cart/', views.cart_page, name='cart_page'),
    path('thankyou/', views.thankyou_page, name='thankyou_page'),
]