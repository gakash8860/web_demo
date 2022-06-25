from attr import fields
from rest_framework import serializers
from .models import UserModel

class UserModelSer(serializers. ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'