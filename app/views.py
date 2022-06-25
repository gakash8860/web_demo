from django.shortcuts import render ,HttpResponse

from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView
from app.serializers import UserModelSer
from .models import UserModel
# Create your views here.
class ListApi(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSer

class CreateApi(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSer
class CreateApi(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSer

class Retriv(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSer
def index( request):
    return HttpResponse ('helll o ')
