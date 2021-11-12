from django.urls import include, path
from booking import views

urlpatterns = [
    path('booking/', include('destiny.urls')),
    path('booking/', include('vehicles.urls')),
    path('booking/select_dest/<str:dest_name>/', views.select_dest, name='select_dest'),
    path('booking/select_vehicle/<str:vehicle_name>/', views.select_vehicle, name='select_vehicle'),
    path('thank_you/', views.thank_you, name='thank_you'),
]