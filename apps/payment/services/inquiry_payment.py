import requests

from django.conf import settings


class InquiryPayment:
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

    def _inquiry(self):
        self.response = requests.post(
            url=settings.VERIFY_PAYMENT_URL,
            json=self.post_json,
            headers=settings.PAYMENT_HEADER
        )

    def _load_inquiry_json(self):
        from ..models import TransactionInquiryResponse
        response = self.response
        response['id_pay_id'] = response['id']
        response.pop('id')
        response['status'] = int(response['status'])
        response['track_id'] = int(response['track_id'])
        return TransactionInquiryResponse(**response)

    def complete_fields(self):
        self._fill_post_json()
        self._inquiry()
        return self._load_inquiry_json()
