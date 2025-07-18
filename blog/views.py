
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer
from django.http import Http404


class BlogAPI(APIView):
    def get(self, request, pk=None):
        if pk:  
            try:
                blog = Blog.objects.get(pk=pk)
            except Blog.DoesNotExist:
                raise Http404
            serializer = BlogSerializer(blog)
            return Response(serializer.data)
        else:  
            blogs = Blog.objects.all()
            serializer = BlogSerializer(blogs, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            raise Http404
        blog.delete()
        return Response({'message': 'Blog deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
