from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('notes/', NoteList.as_view()),
    path('notes/<int:pk>/', NoteDetail.as_view()),
]
