from rest_framework import views, response
from .models import Member

def get_member_data(member):
    return {
        'name' : member.name,
        'role' : member.role,
        'description' : member.description,
        'mentor' : member.mentor,
        'photo' : member.photo
    }

class MemberListView(views.APIView):
    def get(self, request, format=None):
        members = Member.objects.all()
        return response.Response([get_member_data(member) for member in members])