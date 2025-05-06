from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Library, Model, ModelProperty, Material
from .serializers import LibrarySerializer, ModelListSerializer, ModelSerializer, ModelPropertySerializer, \
    MaterialListSerializer

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import Http404

def index(request):
    return HttpResponse("Hello, world. You're at the materials index.")


class LibraryListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, name):
        try:
            return Library.objects.get(library_name=name)
        except Library.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        '''
        Get library details
        '''
        library = self.get_object(name)
        serializer = LibrarySerializer(library)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, name, format=None):
        '''
        Update the library
        '''
        library = self.get_object(name)
        serializer = LibrarySerializer(library, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        library = self.get_object(name)
        library.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ModelLibraryListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all libraries with models
        '''
        libs = Library.objects.all()
        serializer = LibrarySerializer(libs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LibraryModelsListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_objects(self, name):
        try:
            return Model.objects.filter(library__library_name=name)
        except Library.DoesNotExist:
            raise Http404

    # 1. List all
    def get(self, request, name, format=None):
        '''
        List all libraries with models
        '''
        models = self.get_objects(name)
        serializer = ModelListSerializer(models, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LibraryMaterialsListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_objects(self, name):
        try:
            return Material.objects.filter(library__library_name=name)
        except Material.DoesNotExist:
            raise Http404

    # 1. List all
    def get(self, request, name, format=None):
        '''
        List all libraries with models
        '''
        materials = self.get_objects(name)
        serializer = MaterialListSerializer(materials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ModelApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def get_library(self, name):
    #     try:
    #         return Library.objects.filter(library_name=name)
    #     except Library.DoesNotExist:
    #         raise Http404

    def post(self, request, *args, **kwargs):
        '''
        Create a model
        '''
        # library = self.get_library(name)
        serializer = ModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ModelDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, uuid):
        try:
            return Model.objects.get(model_id=uuid)
        except Model.DoesNotExist:
            raise Http404

    # 1. List all
    def get(self, request, uuid, format=None):
        '''
        List all libraries with models
        '''
        model = self.get_object(uuid)
        serializer = ModelSerializer(model)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ModelPropertyApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, uuid):
        try:
            return ModelProperty.objects.filter(model__model_id=uuid)
        except ModelProperty.DoesNotExist:
            raise Http404

    # 1. List all
    def get(self, request, uuid, format=None):
        '''
        List all properties for a model
        '''
        properties = self.get_object(uuid)
        serializer = ModelPropertySerializer(properties, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
