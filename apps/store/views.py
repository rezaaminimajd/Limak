import json

from django.shortcuts import render
from rest_framework.exceptions import NotFound

from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .services.filter import Filter


class StorePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class StorePage(GenericAPIView):
    queryset = Clothe.objects.all()
    serializer_class = ClotheSerializers
    pagination_class = StorePagination

    def get(self, request):
        page = self.paginate_queryset(self.get_queryset())
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(
                data={'clothes': serializer.data})

        data = self.get_serializer(self.get_queryset(), many=True).data
        return Response(data={'clothes': data}, status=status.HTTP_200_OK)

    def post(self, request):
        filters = request.data
        objects = Filter(self.get_queryset(), filters).apply_filters()

        page = self.paginate_queryset(objects)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(
                data={'clothes': serializer.data})

        data = self.get_serializer(objects, many=True).data
        return Response(data={'clothes': data}, status=status.HTTP_200_OK)


class ClothePage(GenericAPIView):
    serializer_class = ClotheSerializers

    def get(self, request, clothe_id):
        obj = get_object_or_404(Clothe, id=clothe_id)
        clothe = self.get_serializer(obj).data
        return Response(data={'clothe': clothe}, status=status.HTTP_200_OK)


class BasketAPIView(GenericAPIView):
    serializer_class = BasketSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        basket = request.user.baskets.filter(payed=False).last()
        data = self.get_serializer(basket).data
        return Response(data={'basket': data}, status=status.HTTP_200_OK)


class ProductInBasketAPIView(GenericAPIView):
    serializer_class = ProductInBasketSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={'details': 'Product added to basket!'},
                            status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id):
        count = json.loads(request.body)['count']
        try:
            count = int(count)
        except ValueError:
            return Response(data={'details': 'Unexpected value'},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            product = self.get_product(product_id)
            product.count -= count
            product.save()
            return Response(status.HTTP_200_OK)

    def delete(self, request, product_id):
        product = self.get_product(product_id)
        product.delete()

        return Response(status=status.HTTP_200_OK)

    def get_product(self, product_id) -> ProductInBasket:
        basket = self.request.user.baskets.filter(payed=False).last()

        if not basket:
            raise NotFound()

        product = ProductInBasket.objects.filter(id=product_id).filter(
            basket=basket).last()
        if not product:
            raise NotFound()

        return product


class EditBasketView(GenericAPIView):
    pass


class ClotheSizeView(GenericAPIView):
    serializer_class = ClotheSizeSerializers

    def get(self, request):
        obj = ClotheSize.objects.all()
        data = self.get_serializer(obj).data
        return Response(data={'clotheSizes': data},
                        status=status.HTTP_200_OK)


class ClotheColorView(GenericAPIView):
    serializer_class = ClotheColorSerializers

    def get(self, request):
        obj = ClotheColor.objects.all()
        data = self.get_serializer(obj).data
        return Response(data={'clotheSizes': data},
                        status=status.HTTP_200_OK)


class ClotheKindView(GenericAPIView):
    serializer_class = ClotheKindSerializers

    def get(self, request):
        obj = ClotheKind.objects.all()
        data = self.get_serializer(obj).data
        return Response(data={'clotheSizes': data},
                        status=status.HTTP_200_OK)


class CategoryView(GenericAPIView):
    serializer_class = CategorySerializers

    def get(self, request):
        obj = Category.objects.all()
        data = self.get_serializer(obj).data
        return Response(data={'clotheSizes': data},
                        status=status.HTTP_200_OK)
