from django.contrib.admin import AdminSite
from .models import Member

class AgileVisionAdmin(AdminSite):
    site_header = 'Agile Vision Administration'

agilevision_admin_site = AgileVisionAdmin(name='admin')
agilevision_admin_site.register(Member)
