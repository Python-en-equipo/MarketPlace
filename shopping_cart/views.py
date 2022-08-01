from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import CartItem, CartSession, Product

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
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()

    # base_url = reverse('ecommerce')
    return redirect("shopping_cart:home")


@login_required
def list_products_cart(request):
    cart_items = None
    total = 0
    quantity = 0
    try:
        cart = CartSession.objects.get(session_id=_get_session_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for item in cart_items:
            total += item.get_subtotal()

        print(f"Total: {total}")
    except CartItem.DoesNotExist:
        pass
    except CartItem.DoesNotExist:
        pass

    return render(request, "cart/cart.html", {"cart_items": cart_items, "total": total})


@login_required
def delete_product_cart(request, product_id):
    cart = CartSession.objects.get(session_id=_get_session_id(request))
    product = Product.objects.get(id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect("shopping_cart:home")


@login_required
def remove_product_cart(request, product_id):
    cart = CartSession.objects.get(session_id=_get_session_id(request))
    product = get_object_or_404(Product, id=product_id)
    item = CartItem.objects.get(product=product, cart=cart)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect("shopping_cart:home")
