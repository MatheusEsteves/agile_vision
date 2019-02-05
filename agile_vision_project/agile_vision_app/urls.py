from django.urls import path
from django.contrib import admin
from .views import UserListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', UserListView.as_view(), name='users'),
]