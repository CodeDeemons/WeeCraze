from django.urls.conf import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register')
]