from django.contrib import admin

# Register your models here.
from . import models

class ProductAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(models.Product, ProductAdmin)