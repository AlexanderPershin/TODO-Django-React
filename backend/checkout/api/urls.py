from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from checkout.api.views import CreateCheckoutSession, WebHook

app_name = "checkout"


urlpatterns = [
    path(
        "create-checkout-session/",
        CreateCheckoutSession.as_view(),
        name="stripe_checkout",
    ),
    path(
        "webhook/",
        WebHook.as_view(),
        name="stripe_webhook",
    ),
]
