from django.contrib import admin
from .models import Vehicle

# Register your models here.
@admin.register(Vehicle)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'model', 'brand', 'desc', 'img_name']