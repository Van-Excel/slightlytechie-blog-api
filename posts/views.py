
from rest_framework import generics
from .models import Posts
from .serializers import PostSerializer

# Create your views here.


class BlogList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
