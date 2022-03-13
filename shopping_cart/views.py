from django.shortcuts import render
from django.http import JsonResponse
from .shopping_cart import ShoppingCart

# Create your views here.
def store_view(request):
  # Este codigo esta probandose
  product = request.GET
  print(product)
  cart = ShoppingCart()
  cart.add_product(product)
  return JsonResponse(cart.cart)
