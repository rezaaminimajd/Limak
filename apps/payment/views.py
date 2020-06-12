from django.shortcuts import redirect

from rest_framework.generics import GenericAPIView

from rest_framework.exceptions import NotFound

# Create your views here.
from apps.store.models import Basket


class PayAPIView(GenericAPIView):

    def post(self, request):
        from .services.create_transaction import CreateTransaction
        basket = Basket.objects.filter(user=request.user).filter(
            payed=False).last()
        if not basket:
            raise NotFound()

        create_transaction = CreateTransaction(order=basket, request=request)
        transaction = create_transaction.run()
        return redirect(transaction.link)
