import requests

from django.conf import settings

from rest_framework import status

from apps.store.models import Basket

from ..models import Transaction


class CreateTransaction:
    def __init__(self, order: Basket, request):
        self.user = request.user
        self.order = order
        self.transaction = None
        self.post_json = {}
        self.response = None
        self.error = False

    def run(self):
        self._fill_post_json()
        self._send_request()
        transaction = self._create_transaction()
        return transaction, self.error

    def _fill_post_json(self):
        self.post_json = {
            'order_id': self.order.id,
            'amount': self.order.total_price,
            'name': self.user.get_full_name(),
            'phone': self.user.profile.phone_number,
            'mail': self.user.email,
            'desc': '',
            'callback': settings.CALLBACK_URL,
            'reseller': None
        }

    def _send_request(self):
        self.response = requests.post(
            url=settings.CREATE_TRANSACTION_URL,
            json=self.post_json,
            headers=settings.PAYMENT_HEADER
        )

    def _create_transaction(self):
        self.post_json['order'] = self.order
        self.post_json['id_pay_id'] = self.response.json.get('id', -1)
        self.post_json['link'] = self.response.json.get('link', -1)
        self.post_json.pop('order_id')
        self.post_json.pop('callback')
        self.post_json.pop('reseller')
        if self.response.status_code != status.HTTP_201_CREATED:
            self.post_json['errors'] = str(self.response.json)
            self.error = True

        return Transaction.objects.create(**self.post_json)
