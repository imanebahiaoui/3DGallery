from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.


class ThreeD(models.Model):
    name = models.CharField(verbose_name="GLB Model Name", max_length=50, null=False, blank=False)
    source = models.FileField(verbose_name="Upload GLB Model", null=False, blank=False, validators=[
        FileExtensionValidator(allowed_extensions=['glb'])], upload_to="static/viewer/source")
    texture_1 = models.FileField(verbose_name="Upload PNG texture 1", null=False, blank=False, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpeg'])], upload_to="static/viewer/textures")
    texture_2 = models.FileField(verbose_name="Upload PNG texture 2", null=False, blank=False, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpeg'])], upload_to="static/viewer/textures")
    texture_3 = models.FileField(verbose_name="Upload PNG texture 3", null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpeg'])], upload_to="static/viewer/textures")
    texture_4 = models.FileField(verbose_name="Upload PNG texture 4", null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpeg'])], upload_to="static/viewer/textures")
    texture_5 = models.FileField(verbose_name="Upload PNG texture 5", null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['png', 'jpeg'])], upload_to="static/viewer/textures")
    created_at = models.DateTimeField(auto_now_add=True)

