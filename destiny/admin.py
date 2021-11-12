from django.contrib import admin
from .models import Destiny

# Register your models here.
@admin.register(Destiny)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'state', 'img_name', 'category', 'short_desc', 'long_desc']