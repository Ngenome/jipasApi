from .models import Comment, Image, Email, Notification, NotificationToken
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class EmailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'


class EmailSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)
    subject = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=1000)
    fromEmail = serializers.EmailField()


class NotificationSerializer(serializers.Serializer):
    class Meta:
        model = Notification
        fields = '__all__'


class NotificationTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationToken
        fields = '__all__'
