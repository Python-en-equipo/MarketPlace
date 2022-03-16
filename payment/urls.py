from . import views
from django.urls import path

app_name = 'payment'

urlpatterns = [
    path('checkout_session/', views.create_checkout_session, name='create-checkout-session'),
    path('test/', views.payment_test, name='test'),
    path('success/', views.payment_success, name='success'),
    path('cancel/', views.payment_cancel, name='cancel'),
]
