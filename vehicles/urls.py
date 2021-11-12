from django.urls.conf import path
from . import views

urlpatterns = [
    path('vehicle/', views.vehicle, name='vehicle'),
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
    path('vehicle_info/<str:vehicle_name>/', views.vehicle_info, name='vehicle_info'),
    path('delete_vehicle/<int:vehicle_id>/', views.delete_vehicle, name='delete_vehicle'),
]