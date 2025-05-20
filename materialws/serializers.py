from rest_framework import serializers
from .models import Library, Model, ModelProperty, Material

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ["library_name", "library_icon", "library_read_only"]

class ModelListSerializer(serializers.ModelSerializer):
    library = serializers.StringRelatedField()
    folder = serializers.StringRelatedField()

    class Meta:
        model = Model
        fields = ["model_id", "library", "folder"]

class ModelSerializer(serializers.ModelSerializer):
    library = serializers.StringRelatedField()
    folder = serializers.StringRelatedField()
    # inherits = serializers.StringRelatedField()

    class Meta:
        model = Model
        fields = ["model_id", "library", "folder", "inherits", "model_type", "model_name",
                  "model_url", "model_description", "model_doi"]

class ModelPropertySerializer(serializers.ModelSerializer):
    properties = serializers.StringRelatedField()

    class Meta:
        model = ModelProperty
        fields = ["properties", "model_property_name", "model_property_display_name", "model_property_type",
                  "model_property_units", "model_property_url", "model_property_description"]

class MaterialListSerializer(serializers.ModelSerializer):
    library = serializers.StringRelatedField()
    folder = serializers.StringRelatedField()
    material_parent = serializers.StringRelatedField()

    class Meta:
        model = Material
        fields = ["material_id", "library", "folder"]
