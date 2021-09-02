from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions
from .models import Note
from .serializers import NoteSerializer
from django.http import HttpResponse, JsonResponse
# Create your views here.

def home(request):
    return HttpResponse('Welcome to django')
class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes=[permissions.AllowAny]


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes=[permissions.AllowAny]

