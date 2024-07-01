import logging
import json
import socketio
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from django.http import JsonResponse
from rest_framework import views, generics, status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from decouple import config

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
import socketio.exceptions
import stripe

from sockets.sockets_client import sio


logger = logging.getLogger(__name__)


class CreateCheckoutSession(views.APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        dataDict = dict(request.data)
        price = dataDict["price"][0]
        product_name = dataDict["product_name"][0]
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        "price_data": {
                            "currency": "usd",
                            "product_data": {
                                "name": product_name,
                            },
                            "unit_amount": price,
                        },
                        "quantity": 1,
                    }
                ],
                mode="payment",
                success_url=config("FRONTEND_CHECKOUT_SUCCESS_URL"),
                cancel_url=config("FRONTEND_CHECKOUT_FAILED_URL"),
            )
            return redirect(checkout_session.url, code=303)
        except Exception as e:
            logger.error(e)
            return e


class WebHook(views.APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        WEBHOOK_SECRET = config("WEBHOOK_SECRET")

        event = None
        payload = request.body
        sig_header = request.META["HTTP_STRIPE_SIGNATURE"]

        try:
            event = stripe.Webhook.construct_event(payload, sig_header, WEBHOOK_SECRET)
        except ValueError as err:
            logger.error(f"Invalid payload {err}")
            raise err
        except stripe.error.SignatureVerificationError as err:
            logger.error(f"Invalid signature {err}")
            raise err

        if event.type == "payment_intent.succeeded":
            payment_intent = event.data.object
            logger.debug(f"payment_intent {payment_intent}")
        elif event.type == "payment_method.attached":
            payment_method = event.data.object
            logger.debug(f"payment_method {payment_method}")
        else:
            logger.debug(f"Unhandled event type {event.type}")

        return JsonResponse(safe=False, data={"message": "Successful action"})
