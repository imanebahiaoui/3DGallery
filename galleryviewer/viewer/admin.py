from django.contrib import admin

# Register your models here.
from viewer.models import ThreeD


class ThreeDAdmin(admin.ModelAdmin):
    list_display = ('name', 'source')


admin.site.register(ThreeD, ThreeDAdmin)
