from django.contrib import admin

from classifier import models

# Register your models here.

@admin.register(models.ImageFile)
class ImageFileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'created_ts']
    ordering = ['name']
    readonly_fields = ('created_ts', 'updated_ts')
    search_fields = ['name']


@admin.register(models.ClassificationType)
class ClassificationTypeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'created_ts']
    ordering = ['name']
    readonly_fields = ('created_ts', 'updated_ts')
    search_fields = ['name']

