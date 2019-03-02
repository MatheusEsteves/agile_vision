from rest_framework import views, response
from .models import *
from .classificator import *
import datetime

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
    
def get_task_label_data(label):
    return {
        'title' : label.title,
        'color' : label.color 
    }

def get_task_data(task):
    return {
        'title' : task.title,
        'labels' : [get_task_label_data(label) for label in task.labels.all()],
        'delivery_date' : str(task.delivery_date),
        'development_time' : task.development_time,
        'validation_time' : task.validation_time,
        'blocking_time' : task.blocking_time,
        'complexity' : get_task_complexity_data(task.complexity) if task.complexity is not None else None
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

def get_project_tasks(slug=None, start_year=None, start_month=None, start_day=None, end_year=None, end_month=None, end_day=None, filter_unfinished_tasks=False):
    projects = Project.objects.filter(slug=slug)
    tasks_object = None
    project = None
    if projects:
        project = projects[0]
        if filter_unfinished_tasks:
            tasks_object = project.tasks.filter(complexity=None)
        else:
            tasks_object = project.tasks.all()

    tasks_list = []
    if project is not None and tasks_object is not None:
        start_date = None
        end_date = None
        if start_year is not None and start_month is not None and start_day is not None:
            start_date = datetime.date(start_year, start_month, start_day)
        if end_year is not None and end_month is not None and end_day is not None:
            end_date = datetime.date(end_year, end_month, end_day)
        
        if start_date is not None and end_date is not None:
            tasks_object = tasks_object.filter(delivery_date__range=(start_date, end_date))
        elif start_date is not None:
            tasks_object = tasks_object.filter(delivery_date__gte=start_date)
        elif end_date is not None:
            tasks_object = tasks_object.filter(delivery_date__lte=end_date)
        tasks_list = list(tasks_object.all())

        if tasks_list is not None and len(tasks_list) > 0:
            tasks_list.sort(key=lambda task:task.delivery_date, reverse=True)
    return tasks_list

class UnfinishedProjectTaskListView(views.APIView):
    def get(self, request, slug=None, start_year=None, start_month=None, start_day=None, end_year=None, end_month=None, end_day=None):
        tasks_list = get_project_tasks(slug, start_year, start_month, start_day, end_year, end_month, end_day, True)
        return response.Response([get_task_data(task) for task in tasks_list])

class ProjectTaskListView(views.APIView):
    def get(self, request, slug=None, start_year=None, start_month=None, start_day=None, end_year=None, end_month=None, end_day=None):
        tasks_list = get_project_tasks(slug, start_year, start_month, start_day, end_year, end_month, end_day, False)
        return response.Response([get_task_data(task) for task in tasks_list])

class ClassificatorTaskView(views.APIView):
    def get(self, request, slug=None, test_development_time=0, test_validation_time=0, test_blocking_time=0):
        complexity_suggestion = ClassificatorTask(slug).get_complexity_suggestion(test_development_time, test_validation_time, test_blocking_time)
        return response.Response(get_task_complexity_data(complexity_suggestion))
                