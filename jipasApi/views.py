from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions
from .models import Image,Comment
from .serializers import ImageSerializer,CommentSerializer
from django.http import HttpResponse, JsonResponse
# Create your views here.

def home(request):
    return HttpResponse('Welcome to django')
class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes=[permissions.IsAuthenticated]
class ImageListAll(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes=[permissions.AllowAny]


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
   # permission_classes=[permissions.AllowAny]
    permission_classes=[permissions.IsAuthenticated]

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
   # permission_classes=[permissions.AllowAny]
    permission_classes=[permissions.IsAuthenticated]


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #permission_classes=[permissions.AllowAny]
    permission_classes=[permissions.IsAuthenticated]
