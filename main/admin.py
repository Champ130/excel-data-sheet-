from django.contrib import admin
from .models import Products
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(Products)
class ProductAdmin(ImportExportModelAdmin):
    list_display =('name','price','category')
