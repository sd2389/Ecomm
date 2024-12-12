from django.shortcuts import render
from django.http import JsonResponse
import json
import os

def home(request):
    return render(request, 'store/login.html')

def products_page(request):
    return render(request, 'store/products.html')

def get_products(request):
    json_file_path = os.path.join(os.path.dirname(__file__), 'data/products.json')
    with open(json_file_path, 'r') as file:
        products = json.load(file)
    
    # randomize the produts for product display
    import random
    if random.random() < 0.8: # 0.8 means 80% of the time data will be randamized
        random.shuffle(products)
    return JsonResponse(products, safe=False)

def cart_page(request):
    return render(request, 'store/cart.html')

def thankyou_page(request):
    return render(request, 'store/thankyou.html')