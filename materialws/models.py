from django.db import models

# Create your models here.
class Library(models.Model):
    # library_id = models.IntegerField(primary_key=True)
    library_name = models.CharField(max_length=512, unique=True)
    library_icon = models.BinaryField(blank=True, editable=True)
    library_read_only = models.BooleanField(default=False)

    def __str__(self):
        return self.library_name

class Folder(models.Model):
    folder_name = models.CharField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    # parent = models.ManyToManyField("self", symmetrical=False, blank=True)

    def __str__(self):
        if len(self.folder_name) > 0 and self.folder_name[0] == '/':
            return self.folder_name
        return '/' + self.folder_name

class Model(models.Model):
    class ModelClasses(models.TextChoices):
        PHYSICAL = 'Physical'
        APPEARANCE = 'Appearance'
    model_id = models.UUIDField(primary_key=True)
    library = models.ForeignKey(Library, related_name='models', on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    inherits = models.ManyToManyField("self", symmetrical=False)
    model_type = models.CharField(choices=ModelClasses)
    model_name = models.CharField(max_length=255)
    model_url = models.CharField(max_length=255, blank=True)
    model_description = models.TextField(blank=True)
    model_doi = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.model_id)

class ModelInheritance(models.Model):
    model = models.ForeignKey(Model, related_name='inherited', on_delete=models.CASCADE)
    inherits = models.ManyToManyField("self", symmetrical=False)

    def __str__(self):
        return str(self.inherits)

class ModelProperty(models.Model):
    model = models.ForeignKey(Model, related_name='properties', on_delete=models.CASCADE)
    model_property_name = models.CharField(max_length=255)
    model_property_display_name = models.CharField(max_length=255, blank=True)
    model_property_type = models.CharField(max_length=255)
    model_property_units = models.CharField(max_length=255, blank=True)
    model_property_url = models.CharField(max_length=255, blank=True)
    model_property_description = models.TextField(blank=True)

class ModelPropertyColumn(models.Model):
    model_property = models.ForeignKey(ModelProperty, related_name='columns', on_delete=models.CASCADE)
    model_property_name = models.CharField(max_length=255)
    model_property_display_name = models.CharField(max_length=255, blank=True)
    model_property_type = models.CharField(max_length=255)
    model_property_units = models.CharField(max_length=255, blank=True)
    model_property_url = models.CharField(max_length=255, blank=True)
    model_property_description = models.TextField(blank=True)

class Material(models.Model):
    material_id = models.UUIDField(primary_key=True)
    library = models.ForeignKey(Library, related_name='materials', on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    material_name = models.CharField(max_length=255)
    material_author = models.CharField(max_length=255, blank=True)
    material_license = models.CharField(max_length=255, blank=True)
    material_parent = models.ManyToManyField("self", symmetrical=False, blank=True)
    material_description = models.TextField(blank=True)
    material_url = models.CharField(max_length=255, blank=True)
    material_reference = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.material_id)

class MaterialTag(models.Model):
    material_tag_name = models.CharField(max_length=255)

class MaterialTagMapping(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    material_tag = models.ForeignKey(MaterialTag, on_delete=models.CASCADE)

class MaterialModels(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

class MaterialPropertyValue(models.Model):
    material = models.ForeignKey(Material, related_name='property_values', on_delete=models.CASCADE)
    model_property_name = models.CharField(max_length=255)
    model_property_type = models.CharField(max_length=255)

class MaterialPropertyStringValue(models.Model):
    # Need to consider the long string table
    material_property_value = models.ForeignKey(MaterialPropertyValue, on_delete=models.CASCADE)
    material_property_value_string = models.TextField()

class MaterialPropertyArrayDescription(models.Model):
    material_property_value = models.ForeignKey(MaterialPropertyValue, on_delete=models.CASCADE)
    model_property_array_rows = models.IntegerField(default=0)
    model_property_array_columns = models.IntegerField(default=0)
    model_property_array_depth = models.IntegerField(default=-1)

class MaterialPropertyArrayValue(models.Model):
    material_property_value = models.ForeignKey(MaterialPropertyValue, on_delete=models.CASCADE)
    model_property_array_row = models.IntegerField(default=0)
    model_property_array_column = models.IntegerField(default=0)
    model_property_array_depth = models.IntegerField(default=-1)
    model_property_array_depth_rows = models.IntegerField(default=-1)
    material_property_value_string = models.TextField()
