from django.contrib import admin
from django.db import models

from .models import Library, Folder, Model
from .BinaryFileInput import BinaryFileInput

class LibraryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.BinaryField: {'widget': BinaryFileInput()},
    }
    fields = ["library_name", "library_icon", "library_read_only"]

class FolderAdmin(admin.ModelAdmin):
    fields = ["folder_name", "library", "parent"]

class ModelAdmin(admin.ModelAdmin):
    fields = ["library", "folder", "model_type", "model_name",
                "model_url", "model_description", "model_doi"]

admin.site.register(Library, LibraryAdmin)
admin.site.register(Folder, FolderAdmin)
admin.site.register(Model, ModelAdmin)
