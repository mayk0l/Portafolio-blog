from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Blog
from rest_blog.serializers import BlogSerializers

@csrf_exempt
@api_view(['GET','POST'])
def listado_blogs(request):
    if request.method == 'GET':
        listadoblogs = Blog.objects.all()
        serializer = BlogSerializers(listadoblogs, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        dataP = JSONParser().parse(request)
        serializer = BlogSerializers (data=dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_blogs(request, id):
    try:
        blog = Blog.objects.get(idBlog = id)
    except Blog.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = BlogSerializers(blog)
        return Response(serializer.data)
    elif request.method =="PUT":
        dataP = JSONParser().parse(request)
        serializer = BlogSerializers(blog, data=dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":          
        blog.delete()
        return Response (status = status.HTTP_204_NO_CONTENT)