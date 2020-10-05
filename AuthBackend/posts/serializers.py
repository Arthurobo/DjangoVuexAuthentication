from rest_framework import serializers
from .models import Post


# output serializer class for  'Mods' model
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
