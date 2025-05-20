from django.contrib import admin
from django.db import models
import nested_admin

from .models import Library, Folder, Model, ModelInheritance, ModelProperty, ModelPropertyColumn
from .BinaryFileInput import BinaryFileInput
from .UUIDInput import UUIDInput

class LibraryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.BinaryField: {'widget': BinaryFileInput()},
    }
    fields = ["library_name", "library_icon", "library_read_only"]

class FolderAdmin(admin.ModelAdmin):
    list_display = ["folder_name", "library"]
    fields = ["folder_name", "library"]

class ModelInheritanceAdmin(admin.StackedInline):
    model = Model
    max_num = 1
    extra = 0
    fields = ["inherits"]

class ModelPropertyColumnAdmin(nested_admin.NestedStackedInline):
    model = ModelPropertyColumn
    extra = 0

class ModelPropertyAdmin(nested_admin.NestedStackedInline):
    model = ModelProperty
    extra = 0
    inlines = [ModelPropertyColumnAdmin,]

class ModelAdmin(nested_admin.NestedModelAdmin):
    list_display = ["model_name", "library", "folder", "model_id"]
    formfield_overrides = {
        models.UUIDField: {'widget': UUIDInput()},
    }
    fields = ["model_id", "library", "folder", "model_type", "model_name",
                "inherits", "model_url", "model_description", "model_doi"]
    # inlines = [ModelInheritanceAdmin,]
    inlines = [ModelPropertyAdmin,]
    radio_fields = {"model_type" : admin.VERTICAL}

admin.site.register(Library, LibraryAdmin)
admin.site.register(Folder, FolderAdmin)
# admin.site.register(ModelInheritance, ModelInheritanceAdmin)
admin.site.register(Model, ModelAdmin)
