from django.urls import path
from .admin import agilevision_admin_site

urlpatterns = [
    path('admin/', agilevision_admin_site.urls), 
]