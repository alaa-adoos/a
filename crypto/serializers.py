from rest_framework import serializers
from .models import Crypto,Post
class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Crypto
        fields="__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields="__all__"