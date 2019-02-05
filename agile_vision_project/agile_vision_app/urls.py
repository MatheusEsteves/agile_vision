from django.urls import path
from .admin import agilevision_admin_site
from .views import UserListView

urlpatterns = [
    path('admin/', agilevision_admin_site.urls),
    path('api/users/', UserListView.as_view(), name='users'),
]