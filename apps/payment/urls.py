from django.urls import path
from . import views

urlpatterns = [
    path('pay', view=views.PayAPIView.as_view(), name='pay'),
    path('call-back', view=views.CallbackPaymentAPIView.as_view(),
         name='pay'),
]
