from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path("api/v1/", include("ecommerce.urls")),
    path("admin/", admin.site.urls),
    path("api/v1/", include("users.urls")),
    path("cart/", include("shopping_cart.urls")),
    path("payment/", include("payment.urls")),
]

# Schema of Documentation API
schema_view = get_schema_view(
    openapi.Info(
        title="Ecommerce API",
        default_version="v1",
        description="Rest API del Ecommerce ",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# swagger
urlpatterns += [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),  # noqa E501
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),  # noqa E501
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
