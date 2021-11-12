from django.urls.conf import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('delete_contact/<int:contact_id>/', views.delete_contact, name='delete_contact')
]