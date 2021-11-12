from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'contact', 'subject', 'adress', 'message']