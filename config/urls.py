from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("ecommerce.urls")),
    path("admin/", admin.site.urls),
    path("user/", include("users.urls")),
    path("cart/", include("shopping_cart.urls"))
    path("payment/", include("payment.urls")),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
