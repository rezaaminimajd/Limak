from rest_framework.generics import get_object_or_404

from limak_backend.celery import app

from apps.store.models import Basket

from .models import Transaction


@app.task(name='check_transaction_status')
def check_transaction_status(id_pay_id, order_id):
    order = get_object_or_404(Basket, id=order_id)
    transaction = get_object_or_404(Transaction, id_pay_id=id_pay_id,
                                    order=order)

