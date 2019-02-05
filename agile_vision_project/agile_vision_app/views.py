from .models import User
from rest_framework import views, response

def get_user_data(user):
    return {
        'name' : user.name
    }

class UserListView(views.APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        return response.Response([get_user_data(user) for user in users])

