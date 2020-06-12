import requests

from django.conf import settings

from rest_framework import status
from rest_framework.generics import get_object_or_404

from ..models import (TransactionStatusTypes as t_status, TransactionCallback,
                      Transaction, ReadyToLoadOrder)


class VerifyPayment:
    def __init__(self, id_pay_id, order_id):
        self.id_pay_id = id_pay_id
        self.order_id = order_id
        self.transaction_callback: TransactionCallback = get_object_or_404(
            TransactionCallback,
            id_pay_id=id_pay_id,
            order_id=order_id
        )

        self.response = None
        self.post_json = {}
        self.error = False

    def run(self):
        self._fill_post_json()
        self._verify()
        self._verify_transaction()
        return self.error

    def _fill_post_json(self):
        self.post_json = {
            'id': self.id_pay_id,
            'order_id': self.order_id
        }

    def _verify(self):
        self.response = requests.post(
            url=settings.VERIFY_PAYMENT_URL,
            json=self.post_json,
            headers=settings.PAYMENT_HEADER
        )

    def _verify_transaction(self):
        if self.response.status_code != status.HTTP_200_OK:
            self.transaction_callback.errors += str(self.response.json()())
            self.transaction_callback.status = t_status.ERROR
            self.error = True
        elif self.response.json()['status'] == t_status.PAYMENT_VERIFIED:
            self.transaction_callback.status = t_status.PAYMENT_VERIFIED

            ReadyToLoadOrder.objects.create(
                order=self.transaction_callback.transaction.order,
                user=self.transaction_callback.transaction.order.user,
            )

        self.transaction_callback.save()
