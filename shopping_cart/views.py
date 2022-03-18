from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .shopping_cart import ShoppingCart
from .models import CartItem, CartSession, Product
from ecommerce.models import Image
# from ecommerce.models import Product


def _get_session_id(request):
    cart_session = request.session.session_key
    if not cart_session:
        cart_session = request.session.create()
    return cart_session


@login_required
# Create your views here.
def add_product_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    try:
        cart = CartSession.objects.get(session_id=_get_session_id(request))
    except CartSession.DoesNotExist:
        cart = CartSession.objects.create(session_id=_get_session_id(request))

    cart.save()
    print("Added product")

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        print("Added new product")
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()

    # base_url = reverse('ecommerce')
    return redirect("ecommerce:home")


def list_products_cart(request):
    products = Product.objects.all()
    images = Image.objects.all()
    return render(request, 'cart/cart.html', {"products": products, "images": images})
