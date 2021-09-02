from .models import Comment,Image
from rest_framework  import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields ='__all__'
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields ='__all__'
