from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('images/', ImageList.as_view()),
    path('imagelist/', ImageListAll.as_view()),
    path('images/<int:pk>/', ImageDetail.as_view()),
    path('comments/',CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    path('sendemail/',SendEmail.as_view()),
]
