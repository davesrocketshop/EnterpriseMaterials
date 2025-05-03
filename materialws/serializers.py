from rest_framework import serializers
from .models import Library, Model, Material

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ["library_name", "library_icon", "library_read_only", "library_modified"]

class ModelListSerializer(serializers.ModelSerializer):
    library = serializers.StringRelatedField()
    folder = serializers.StringRelatedField()

    class Meta:
        model = Model
        fields = ["model_id", "library", "folder"]

class ModelSerializer(serializers.ModelSerializer):
    library = serializers.StringRelatedField()
    folder = serializers.StringRelatedField()

    class Meta:
        model = Model
        fields = ["model_id", "library", "folder", "model_type", "model_name", "model_url",
                  "model_description", "model_doi"]

class MaterialListSerializer(serializers.ModelSerializer):
    library = serializers.StringRelatedField()
    folder = serializers.StringRelatedField()
    material_parent = serializers.StringRelatedField()

    class Meta:
        model = Material
        fields = ["material_id", "library", "folder"]
