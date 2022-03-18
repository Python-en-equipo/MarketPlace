from django.conf import settings
import stripe
from config.settings import STRIPE_PRIVATE_KEY, STRIPE_WEBHOOK_KEY
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

YOUR_DOMAIN = 'http://127.0.0.1:8000'

stripe.api_key = STRIPE_PRIVATE_KEY

def payment_test(request):
    return render(request, 'payment/payment.html')

def payment_success(request):
    return render(request, 'payment/success.html')

def payment_cancel(request):
    return render(request, 'payment/cancel.html')

def create_checkout_session(request):
    if request.method == 'POST':
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'mxn', # moneda de pago
                            'product_data':{ # informacion del producto, tambien se puede agregar descripcion, pero no veo necesario
                                'name': 'microfono',
                            },
                            'unit_amount': 1000, # precio del articulo
                        },
                        'quantity': 2, # cantidad de productos que se comprara
                    }
                ],
                # customer_email=self.request.user.email, # for pass user email
                payment_method_types = ['card','oxxo'],
                billing_address_collection='required', # pedir direccion
                mode='payment',
                success_url=request.build_absolute_uri(reverse_lazy('payment:success')),
                cancel_url=request.build_absolute_uri(reverse_lazy('payment:cancel')),
            )
        except Exception as e:
            print(e)
            return str(e)

        return redirect(checkout_session.url)


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_KEY
            )
    except ValueError as e:
        # Invalid payload
        print('error')
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print('error')
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fulfill the purchase...
        fulfill_order(session)
        print('éxito')
        # Passed signature verification
        return HttpResponse(status=200)

def fulfill_order(session):
    customer_email = session['customer_details']['email']
    customer_shipping = session['shipping']
    

    print(settings.EMAIL_HOST_USER)

    send_mail(
        subject="Orden de compra",
        # TODO, NO GUARDA EL VALOR DE customer_shipping
        message=f"Gracias por tu compra, te la enviaremos a {customer_shipping}",
        recipient_list=[customer_email],
        from_email=settings.EMAIL_HOST_USER,
        fail_silently=False,
    )

    print("Fulfilling order")
