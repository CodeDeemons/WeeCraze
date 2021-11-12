"""WeeCraze URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.urls import include, path

admin.site.site_header = "WeeCraze Admin"
admin.site.site_title = "WeeCraze Portal"
admin.site.index_title = "Welcome to WeeCraze (-- SuperUser --)"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('register.urls')),
    path('', include('login.urls')),
    path('', include('about.urls')),
    path('', include('contact.urls')),
    path('', include('booking.urls')),
    path('', include('vehicles.urls')),
    # path('hotels/', include('hotels.urls')),
]