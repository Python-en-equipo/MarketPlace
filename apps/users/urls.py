from django.urls import path
from . import views

# no borrar porque los templates usan la appname
app_name = "users"

urlpatterns = [    
    path("vendor_register/", views.vendor_register, name="vendor_register"),
]
