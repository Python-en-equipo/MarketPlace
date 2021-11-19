from django.contrib import admin
import debug_toolbar
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecommerce/', include('ecommerce.urls')),
    path('__debug__/', include(debug_toolbar.urls))
]
