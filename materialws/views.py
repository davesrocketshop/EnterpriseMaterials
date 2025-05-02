from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Library
from .serializers import LibrarySerializer

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the materials index.")


class LibraryListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all libraries
        '''
        libs = Library.objects.all()
        serializer = LibrarySerializer(libs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create a library
        '''
        data = {
            'library_name': request.data.get('library_name'), 
            'library_icon': request.data.get('library_icon'), 
            'library_read_only': request.data.get('library_read_only'), 
        }
        serializer = LibrarySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LibraryDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all libraries with models
        '''
        libs = Library.objects.all()
        serializer = LibrarySerializer(libs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
def library_detail(request, name):
    """
    Retrieve information for a specific library
    """
    try:
        library = Library.objects.get(library_name=name)
    except Library.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LibrarySerializer(library)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

class ModelLibraryListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all libraries with models
        '''
        libs = Library.objects.all()
        serializer = LibrarySerializer(libs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MaterialLibraryListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all libraries with models
        '''
        libs = Library.objects.all()
        serializer = LibrarySerializer(libs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
