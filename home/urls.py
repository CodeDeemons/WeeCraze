from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', views.clients, name='clients'),
    path('delete_client/<int:client_id>/', views.delete_client, name='delete_client'),
]