from django.shortcuts import render

from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class StorePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class StorePage(GenericAPIView):
    queryset = Clothe.objects.all()
    serializer_class = ClotheSerializers
    pagination_class = StorePagination

    def get(self):
        data = self.get_serializer(self.get_queryset(), many=True).data
        return Response(data={'clothes': data}, status=status.HTTP_200_OK)


class ClothePage(GenericAPIView):
    serializer_class = ClotheSerializers

    def get(self, clothe_id):
        obj = get_object_or_404(Clothe, id=clothe_id)
        clothe = self.get_serializer(obj).data
        return Response(data={'clothe': clothe}, status=status.HTTP_200_OK)


class EditBasketView(GenericAPIView):
    pass


class ClotheSizeView(GenericAPIView):
    serializer_class = ClotheSizeSerializers

    def get(self):
        obj = ClotheSize.objects.all()
        data = self.get_serializer(obj).data
        return Response(data={'clotheSizes': data},
                        status=status.HTTP_200_OK)


class ClotheColorView(GenericAPIView):
    serializer_class = ClotheColorSerializers

    def get(self):
        obj = ClotheColor.objects.all()
        data = self.get_serializer(obj).data
        return Response(data={'clotheSizes': data},
                        status=status.HTTP_200_OK)


class ClotheKindView(GenericAPIView):
    serializer_class = ClotheKindSerializers

    def get(self):
        obj = ClotheKind.objects.all()
        data = self.get_serializer(obj).data
        return Response(data={'clotheSizes': data},
                        status=status.HTTP_200_OK)


class CategoryView(GenericAPIView):
    serializer_class = CategorySerializers

    def get(self):
        obj = Category.objects.all()
        data = self.get_serializer(obj).data
        return Response(data={'clotheSizes': data},
                        status=status.HTTP_200_OK)
