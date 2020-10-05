from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


# View for 'Mods' model
class PostView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)  # checks if user is authenticated to view the model objects

    def get_queryset(self):
        return Post.objects.all()  # return all model objects

    def get(self, request, *args, **kwargs):  # GET request handler for the model
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_class = [IsAuthenticated,]