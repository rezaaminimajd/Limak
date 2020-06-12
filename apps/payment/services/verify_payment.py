import requests

from django.conf import settings


class VerifyPayment:
    def __init__(self, id_pay_id, order_id):
        self.id_pay_id = id_pay_id
        self.order_id = order_id
        self.response = None
        self.post_json = {}

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
        pass
