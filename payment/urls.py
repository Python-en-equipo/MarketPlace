from django.urls import path

from . import views

app_name = "payment"

urlpatterns = [
    path("checkout-session/", views.create_checkout_session, name="create-checkout-session"),
    path("webhooks/stripe/", views.stripe_webhook, name="stripe-webhook"),
    path("test/", views.payment_test, name="test"),
    path("success/", views.payment_success, name="success"),
    path("cancel/", views.payment_cancel, name="cancel"),
]
