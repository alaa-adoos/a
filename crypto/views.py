from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from .serializers import  CryptoSerializer,PostSerializer
from .models import Crypto,Post
class CryptoListView(ListCreateAPIView):
    queryset=Crypto.objects.all()
    serializer_class=CryptoSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

class CryptoDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Crypto.objects.all()
    serializer_class=CryptoSerializer
    permission_classes=[IsOwnerOrReadOnly]

class PostListView(ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]