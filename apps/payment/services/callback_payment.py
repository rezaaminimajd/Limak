import json
import datetime

from rest_framework.generics import get_object_or_404

from ..models import (TransactionStatusTypes as t_status, Transaction,
                      TransactionCallback)


class CallbackPayment:

    def __init__(self, request):
        self.user = request.user
        self.json = json.loads(request.body)
        self.transaction_callback = TransactionCallback()
        self.verify = False

    def run(self):
        self._verify_information()
        return (self.verify, self.transaction_callback.id_pay_id,
                self.transaction_callback.order_id)

    def _verify_information(self):
        self.json['id_pay_id'] = int(self.json['id'])
        self.json.pop('id')
        self.json['track_id'] = int(self.json['track_id'])
        self.json['amount'] = int(self.json['amount'])
        self.json['date'] = datetime.datetime.fromtimestamp(
            int(self.json['date'])
        )

        transaction = get_object_or_404(
            Transaction,
            id_pay_id=self.transaction_callback.id_pay_id,
            order_id=self.transaction_callback.order_id
        )
        self.json['transaction'] = transaction

        self.transaction_callback = TransactionCallback(**self.json)

        if not transaction.amount == self.transaction_callback.amount:
            self.transaction_callback.errors += (
                f'Amounts not compatible: Transaction = {transaction.amount}'
                f'  Callback = {self.transaction_callback.amount}\n\n'
            )
        self.transaction_callback.errors += t_status.TYPES_DICT[
            self.transaction_callback.status
        ]
        if self.transaction_callback.status == \
                t_status.WAITING_FOR_PAYMENT_VERIFICATION:
            self.verify = True
        self.transaction_callback.save()
