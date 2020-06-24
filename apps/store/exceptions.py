from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import APIException
from rest_framework import status


class OutOfStock(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Out of stock')
    default_code = _('out_of_stock')
