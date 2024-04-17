from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import permissions
from .models import *
from .serializers import *
from rest_framework.response import Response
# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class LevelViewset(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer

class CoordsViewset(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer

class ImageViewset(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer

class PerevalViewset(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filterset_fields =('tourist_id__email',)

    def create(selfself, request, *args, **kwargs):
      serializer=PerevalSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({
            'status':status.HTTP_200_OK,
            'message':None,
            'id':serializer.data['id'],
         })
      if status.HTTP_400_BAD_REQUEST:
         return Response({
            'status':status.HTTP_400_BAD_REQUEST,
            'message': 'Bad Request',
            'id': None,
         })
      if status.HTTP_500_INTERNAL_SERVER_ERROR:
         return Response({
            'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'message':'Ошибка подключения к базе данных',
            'id': None,
         })
        
    def partial_update(self, request, *args, **kwargs):
        pereval=self.get_object()
        if pereval.status=='new':
            serializers=PerevalSerializer(pereval, data=request.data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response({
                    'state': '1',
                    'message': 'Запись изменена'
                })
            else:
                return Response({
                    'status': '0',
                    'message': serializers.errors
                })
        else:
            return Response({
                'state': '0',
                'message': f'Отклонено! Причина: {pereval.get_status_display()}'
            })
       