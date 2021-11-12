from django.urls.conf import path
from . import views

urlpatterns = [
    path('destiny/', views.destiny, name='destiny'),
    path('add_dest/', views.add_dest, name='add_dest'),
    path('dest_info/<str:dest_name>/', views.dest_info, name='dest_info'),
    path('delete_dest/<int:dest_id>/', views.delete_dest, name='delete_dest'),
]