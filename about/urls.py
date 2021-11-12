from django.urls.conf import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about')
]