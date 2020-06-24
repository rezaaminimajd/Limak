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

        create_transaction = CreateTransaction(order=basket,
                                               request=request)

        transaction, error = create_transaction.run()
        if error:
            return Response(data={'detail': _('Error occurred')},
                            status=status.HTTP_400_BAD_REQUEST)

        # return redirect(transaction.link)
        return Response(data={'link': transaction.link})


class CallbackPaymentAPIView(GenericAPIView):

    def post(self, request):
        from .services.callback_payment import CallbackPayment
        from .services.verify_payment import VerifyPayment

        callback_payment = CallbackPayment(request=request)
        verify, id_pay_id, order_id = callback_payment.run()

        if not verify:
            return Response(data={'detail': _('Error occurred')},
                            status=status.HTTP_400_BAD_REQUEST)

        verify_payment = VerifyPayment(
            id_pay_id=id_pay_id,
            order_id=order_id
        )
        error = verify_payment.run()

        if error:
            return Response(data={'detail': _('Error occurred!')},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code': order_id}, status=status.HTTP_200_OK)
