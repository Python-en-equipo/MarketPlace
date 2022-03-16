import stripe
from config.settings import STRIPE_PRIVATE_KEY
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

YOUR_DOMAIN = 'http://127.0.0.1:8000'

stripe.api_key = STRIPE_PRIVATE_KEY
def create_checkout_session(request):
    if request.method == 'POST':
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd', # moneda de pago
                            'product_data':{ # informacion del producto, tambien se puede agregar descripcion, pero no veo necesario
                                'name': 'microfono',
                            },
                            'unit_amount': 1000, # precio del articulo
                        },
                        'quantity': 2, # cantidad de productos que se comprara
                    }
                ],
                mode='payment',
                success_url=request.build_absolute_uri(reverse_lazy('payment:success')),
                cancel_url=request.build_absolute_uri(reverse_lazy('payment:cancel')),
            )
        except Exception as e:
            print(e)
            return str(e)

        return redirect(checkout_session.url)

def payment_test(request):
    return render(request, 'payment/payment.html')

def payment_success(request):
    return render(request, 'payment/success.html')

def payment_cancel(request):
    return render(request, 'payment/cancel.html')

