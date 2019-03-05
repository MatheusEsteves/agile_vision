from rest_framework import views, response
from .models import *
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

def filter_tasks_by_date_interval(task_entities=None, start_date=None, end_date=None):
    tasks_list = []
    if task_entities is not None:
        if start_date is not None and end_date is not None:
            task_entities = task_entities.filter(delivery_date__range=(start_date, end_date))
        elif start_date is not None:
            task_entities = task_entities.filter(delivery_date__gte=start_date)
        elif end_date is not None:
            task_entities = task_entities.filter(delivery_date__lte=end_date)
        tasks_list = list(task_entities.all())

        if tasks_list is not None and len(tasks_list) > 0:
            tasks_list.sort(key=lambda task:task.delivery_date, reverse=True)
    return tasks_list

def get_finished_project_tasks(project=None, complexity=None, start_date=None, end_date=None):
    if project is not None:
        if complexity is not None:
            task_entities = project.tasks.filter(complexity=complexity)
            tasks_list = filter_tasks_by_date_interval(task_entities, start_date, end_date)
            return [get_task_data(task) for task in tasks_list]
        else:
            finished_project_tasks_dict = {}
            all_task_complexities = TaskComplexity.objects.all()
            if all_task_complexities is not None:
                for task_complexity in all_task_complexities:
                    complexity_name = task_complexity.name
                    tasks = get_finished_project_tasks(project, task_complexity, start_date, end_date)
                    finished_project_tasks_dict[complexity_name] = tasks
            return finished_project_tasks_dict
    else:
        return []

def get_unfinished_project_tasks(slug=None, start_date=None, end_date=None):
    projects = Project.objects.filter(slug=slug)
    task_entities = None
    project = None
    if projects:
        project = projects[0]
        task_entities = project.tasks.filter(complexity=None)
    return filter_tasks_by_date_interval(task_entities, start_date, end_date)

def get_all_project_tasks(slug=None, start_date=None, end_date=None):
    projects = Project.objects.filter(slug=slug)
    task_entities = None
    project = None
    if projects:
        project = projects[0]
        task_entities = project.tasks.all()
    return filter_tasks_by_date_interval(task_entities, start_date, end_date)


def convert_string_to_date_object(str_date=None):
    if str_date is None:
        return None
    else:
        str_year, str_month, str_day = str_date.split('-')
        return datetime.date(int(str_year), int(str_month), int(str_day))

class UnfinishedProjectTaskListView(views.APIView):
    def get_unfinished_project_tasks(self, slug=None, start_date=None, end_date=None):
        start_date_object = convert_string_to_date_object(start_date)
        end_date_object = convert_string_to_date_object(end_date)
        return get_unfinished_project_tasks(slug, start_date_object, end_date_object)

    def get(self, request, slug=None, start_date=None, end_date=None):
        tasks_list = self.get_unfinished_project_tasks(slug, start_date, end_date)
        return response.Response([get_task_data(task) for task in tasks_list])

class UnfinishedProjectTaskCount(views.APIView):
    def get(self, request, slug=None, start_date=None, end_date=None):
        tasks_list = UnfinishedProjectTaskListView().get_unfinished_project_tasks(slug, start_date, end_date)
        return response.Response(len(tasks_list))

class FinishedProjectTaskListView(views.APIView):
    def get_finished_project_tasks(self, slug=None, start_date=None, end_date=None, complexity_weight=None):
        task_complexities = TaskComplexity.objects.filter(weight=complexity_weight)
        complexity = None
        if task_complexities:
            complexity = task_complexities[0]
        projects = Project.objects.filter(slug=slug)
        project = None
        if projects:
            project = projects[0]
        task_entities = None

        start_date_object = convert_string_to_date_object(start_date)
        end_date_object = convert_string_to_date_object(end_date)
        tasks_list = get_finished_project_tasks(project, complexity, start_date_object, end_date_object)
        return tasks_list

    def get(self, request, slug=None, start_date=None, end_date=None, complexity_weight=None):
        tasks_list = self.get_finished_project_tasks(slug, start_date, end_date, complexity_weight)
        return response.Response(tasks_list)

class FinishedProjectTaskCount(views.APIView):
    def get(self, request, slug=None, start_date=None, end_date=None, complexity_weight=None):
        tasks_list = FinishedProjectTaskListView().get_finished_project_tasks(slug, start_date, end_date, complexity_weight)
        task_count_structure = None
        if complexity_weight is not None:
            task_count_structure = len(tasks_list)
        else:
            task_count_structure = {}
            for complexity_name in tasks_list:
                task_count_structure[complexity_name] = len(tasks_list[complexity_name])
        return response.Response(task_count_structure)

class ProjectTaskListView(views.APIView):
    def get_all_project_tasks(self, slug=None, start_date=None, end_date=None):
        start_date_object = convert_string_to_date_object(start_date)
        end_date_object = convert_string_to_date_object(end_date)
        return get_all_project_tasks(slug, start_date_object, end_date_object)

    def get(self, request, slug=None, start_date=None, end_date=None):
        tasks_list = self.get_all_project_tasks(slug, start_date, end_date)
        return response.Response([get_task_data(task) for task in tasks_list])

class ProjectTaskCount(views.APIView):
    def get(self, request, slug=None, start_date=None, end_date=None):
        tasks_list = ProjectTaskListView().get_all_project_tasks(slug, start_date, end_date)
        return response.Response(len(tasks_list))
                