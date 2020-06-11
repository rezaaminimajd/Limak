from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import InformationSerializers
from .models import Information


class InformationView(GenericAPIView):
    serializer_class = InformationSerializers
    queryset = Information.objects.all()

    def get(self, request):
        information = self.get_serializer(self.get_queryset().first()).data
        return Response(data={'details': information},
                        status=status.HTTP_200_OK)
