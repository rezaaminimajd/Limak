from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('clothe/<str:clothe_id>', view=views.ClothePage.as_view(),
         name='clothe'),
    path('store_page', view=views.StorePage.as_view(), name='store'),
    path('clothe-kind', view=views.ClotheKindView.as_view(),
         name='clothe_kind'),
    path('clothe-size', view=views.ClotheSizeView.as_view()),
    path('clothe-color', view=views.ClotheColorView.as_view()),
    path('category', view=views.CategoryView.as_view()),
    path('basket', view=views.BasketAPIView.as_view(), name='basket'),
    path('basket/add', view=views.ProductInBasketAPIView.as_view(),
         name='basket_add'),
    path('basket/edit/<str:product_id>',
         view=views.ProductInBasketAPIView.as_view(),
         name='basket_edit'),
]
