import requests

from django.conf import settings

from apps.store.models import Basket

class CreateTransaction:
    def __init__(self, order: Basket, request):
        self.user = request.user
        self.order = order
        self.post_json = {}
        self.response = ''


    def _fill_post_json(self):
        post_json = {
            'order_id': self.order.id,
            'amount'

        }

    def _send_request(self):
        response = requests.post(
            url=settings.CREATE_TRANSACTION_URL,
            json=
        )