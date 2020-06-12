from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from apps.store.models import Basket


class PayAPIView(GenericAPIView):

    def post(self, request):
        from .services.create_transaction import CreateTransaction
        basket = Basket.objects.filter(user=request.user).filter(
            payed=False).last()
        if not basket:
            raise NotFound()

        create_transaction, error = CreateTransaction(order=basket,
                                                      request=request)
        if error:
            return Response(data={'detail': _('Error occurred')},
                            status=status.HTTP_400_BAD_REQUEST)
        
        transaction = create_transaction.run()
        return redirect(transaction.link)


class CallbackPaymentAPIView(GenericAPIView):

    def post(self, request):
        from .services.callback_payment import CallbackPayment
        callback_payment = CallbackPayment(request=request)
        verify = callback_payment.run()

        if not verify:
            return Response(data={'detail': _('Error occurred')},
                            status=status.HTTP_400_BAD_REQUEST)
