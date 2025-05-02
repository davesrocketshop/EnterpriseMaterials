from rest_framework import serializers
from .models import Library

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ["library_name", "library_icon", "library_read_only", "library_modified"]
