# posts/api/serializers.py

from ..models import Post,Comment
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'is_featured','categories','userId','image') # if not declared, 

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
         model = Comment
         fields =  ('content','reply')