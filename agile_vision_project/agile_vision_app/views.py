from rest_framework import views, response
from .models import *

def get_member_data(member):
    return {
        'name' : member.name,
        'username' : member.username,
        'email' : member.email,
        'role' : member.role,
        'description' : member.description,
        'mentor' : member.mentor,
        'next_holidays_start_date' : str(member.next_holidays_start_date),
        'next_holidays_end_date' : str(member.next_holidays_end_date),
        'last_one_one_meeting_date' : str(member.last_one_one_meeting_date),
        'last_one_one_meeting_manager' : member.last_one_one_meeting_manager
    }

def get_indicator_vision_data(indicator_vision):
    return {
        'name' : indicator_vision.name,
        'weight' : indicator_vision.weight
    }

def get_indicator_type_data(indicator_type):
    return {
        'name' : indicator_type.name 
    }

def get_indicator_item_data(indicator_item):
    return {
        'indicator_type' : indicator_item.indicator_type.name,
        'indicator_vision_currently_month' : 
            get_indicator_vision_data(indicator_item.indicator_vision_currently_month),
        'indicator_vision_next_month' : 
            get_indicator_vision_data(indicator_item.indicator_vision_next_month)
    }

def get_project_data(project):
    return {
        'slug' : project.slug,
        'name' : project.name,
        'description' : project.description,
        'client' : project.client
    }

def get_team_data(team):
    return {
        'slug' : team.slug,
        'name' : team.name,
        'description' : team.description,
        'email' : team.email
    }

def get_task_complexity_data(task_complexity):
    return {
        'name' : task_complexity.name,
        'weight' : task_complexity.weight
    }

def get_task_data(task):
    return {
        'development_time' : task.development_time,
        'validation_time' : task.validation_time,
        'blocking_time' : task.blocking_time,
        'complexity' : get_task_complexity_data(task.complexity)
    }

class MemberListView(views.APIView):
    def get(self, request, username=None):
        members = []
        if username is None:
            members = Member.objects.all()
        else:
            members = Member.objects.filter(username=username)
        return response.Response([get_member_data(member) for member in members])

class IndicatorVisionListView(views.APIView):
    def get(self, request, format=None):
        indicator_visions = IndicatorVision.objects.all()
        return response.Response([get_indicator_vision_data(indicator_vision) for indicator_vision in indicator_visions])

class IndicatorTypeListView(views.APIView):
    def get(self, request, format=None):
        indicator_types = IndicatorType.objects.all()
        return response.Response([get_indicator_type_data(indicator_type) for indicator_type in indicator_types])

class ProjectListView(views.APIView):
    def get(self, request, slug=None):
        projects = []
        if slug is None:
            projects = Project.objects.all()
        else:
            projects = Project.objects.filter(slug=slug)
        return response.Response([get_project_data(project) for project in projects])

class ProjectMemberListView(views.APIView):
    def get(self, request, slug=None):
        projects = Project.objects.filter(slug=slug)
        members = []
        if projects:
            project = projects[0]
            members = project.members.all()
        return response.Response([get_member_data(member) for member in members])

class ProjectIndicatorListView(views.APIView):
    def get(self, request, slug=None):
        projects = Project.objects.filter(slug=slug)
        indicators = []
        if projects:
            project = projects[0]
            indicators = project.indicators.all()
        return response.Response([get_indicator_item_data(indicator) for indicator in indicators])

class TeamListView(views.APIView):
    def get(self, request, slug=None):
        teams = []
        if slug is None:
            teams = Team.objects.all()
        else:
            teams = Team.objects.filter(slug=slug)
        return response.Response([get_team_data(team) for team in teams])

class TeamProjectListView(views.APIView):
    def get(self, request, slug=None):
        teams = Team.objects.filter(slug=slug)
        projects = []
        if teams:
            team = teams[0]
            projects = team.projects.all()
        return response.Response([get_project_data(project) for project in projects])

class TeamMemberListView(views.APIView):
    def get(self, request, slug=None):
        teams = Team.objects.filter(slug=slug)
        members = []
        if teams:
            team = teams[0]
            projects = team.projects.all()
            for project in projects:
                project_members = list(project.members.all())
                members = members + project_members
        return response.Response([get_member_data(member) for member in members])

class TaskComplexityListView(views.APIView):
    def get(self, request, format=None):
        task_complexities = TaskComplexity.objects.all()
        return response.Response([get_task_complexity_data(task_complexity) for task_complexity in task_complexities])

class ProjectTaskListView(views.APIView):
    def get(self, request, slug=None):
        projects = Project.objects.filter(slug=slug)
        tasks = []
        if projects:
            project = projects[0]
            tasks = project.tasks.all()
        return response.Response([get_task_data(task) for task in tasks])