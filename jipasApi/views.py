from django.shortcuts import render
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushServerError,
    PushTicketError,
)
from requests.exceptions import ConnectionError, HTTPError
from rest_framework.views import APIView
from .models import Image, Comment, NotificationToken
from .serializers import ImageSerializer, CommentSerializer, EmailSerializer, NotificationSerializer, NotificationTokenSerializer
from django.http import HttpResponse, JsonResponse
# Create your views here.
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
username = 'jipasmail@gmail.com'
password = '@jipastentsail'


def send_mail(text='blank', subject='Hello word', from_email='', to_emails=[]):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    html_part = MIMEText(
        f"<div><h3>{text}</h3>from<a href='mailto:{from_email}'>{from_email}</a></div>", 'html')
    msg.attach(html_part)
    msg_str = msg.as_string()
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()


def home(request):
    return HttpResponse('Welcome to django')


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class ImageListAll(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.AllowAny]


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
   # permission_classes=[permissions.AllowAny]
    permission_classes = [permissions.IsAuthenticated]


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
   # permission_classes=[permissions.AllowAny]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TokenList(generics.ListCreateAPIView):
    queryset = NotificationToken.objects.all()
    serializer_class = NotificationTokenSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SendyEmail(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
   # permission_classes=[permissions.AllowAny]
    permission_classes = [permissions.IsAuthenticated]


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes=[permissions.AllowAny]
    permission_classes = [permissions.IsAuthenticated]


class SendEmail(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def post(self, request, format=None):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():

            send_mail(text=request.data["email"], subject=request.data["subject"],
                      from_email=request.data["fromEmail"], to_emails=['jipasmail@gmail.com'])

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_push_message(token, message, extra=None):
    try:
        response = PushClient().publish(
            PushMessage(to=token,
                        body=message,
                        data=extra))
    except PushServerError as exc:
        # Encountered some likely formatting/validation error.
        print('error sir')
        raise
    except (ConnectionError, HTTPError) as exc:
        # Encountered some Connection or HTTP error - retry a few times in
        # case it is transient.
        print(ConnectionError)

    try:

        response.validate_response()
    except DeviceNotRegisteredError:
        print("device Not Registered")
    except PushTicketError as exc:
        print('Error 2')


class SendNotification(APIView):
    def post(self, request, format=None):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            send_push_message(
                request.data["token"], request.data["Notification"], extra=None)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
