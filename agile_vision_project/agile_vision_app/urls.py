from django.urls import path, re_path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/members', MemberListView.as_view(), name='members'),
    path('api/members/<username>', MemberListView.as_view(), name='members'),
    path('api/indicatorvisions', IndicatorVisionListView.as_view(), name='indicator_visions'),
    path('api/indicatortypes', IndicatorTypeListView.as_view(), name='indicator_types'),
    path('api/projects', ProjectListView.as_view(), name='projects'),
    path('api/projects/<slug>', ProjectListView.as_view(), name='projects'),
    path('api/projects/<slug>/members', ProjectMemberListView.as_view(), name='project_members'),
    path('api/projects/<slug>/indicators', ProjectIndicatorListView.as_view(), name='project_indicators'),
    path('api/teams', TeamListView.as_view(), name='teams'),
    path('api/teams/<slug>', TeamListView.as_view(), name='teams'),
    path('api/teams/<slug>/projects', TeamProjectListView.as_view(), name='team_projects'),
    path('api/teams/<slug>/members', TeamMemberListView.as_view(), name='team_members'),
    path('api/taskcomplexities', TaskComplexityListView.as_view(), name='task_complexities'),
    
    path('api/projects/<slug>/unfinished_tasks/range_date/<start_date>/<end_date>', UnfinishedProjectTaskListView.as_view(), name='unfinished_project_tasks'),
    path('api/projects/<slug>/unfinished_tasks/start_date/<start_date>', UnfinishedProjectTaskListView.as_view(), name='unfinished_project_tasks'),
    path('api/projects/<slug>/unfinished_tasks/end_date/<end_date>', UnfinishedProjectTaskListView.as_view(), name='unfinished_project_tasks'),

    path('api/projects/<slug>/finished_tasks/range_date/<start_date>/<end_date>/<int:complexity_weight>', FinishedProjectTaskListView.as_view(), name='finished_project_tasks'),
    path('api/projects/<slug>/finished_tasks/start_date/<start_date>/<int:complexity_weight>', FinishedProjectTaskListView.as_view(), name='finished_project_tasks'),
    path('api/projects/<slug>/finished_tasks/end_date/<end_date>/<int:complexity_weight>', FinishedProjectTaskListView.as_view(), name='finished_project_tasks'),

    path('api/projects/<slug>/finished_tasks/range_date/<start_date>/<end_date>', FinishedProjectTaskListView.as_view(), name='finished_project_tasks'),
    path('api/projects/<slug>/finished_tasks/start_date/<start_date>', FinishedProjectTaskListView.as_view(), name='finished_project_tasks'),
    path('api/projects/<slug>/finished_tasks/end_date/<end_date>', FinishedProjectTaskListView.as_view(), name='finished_project_tasks'),

    path('api/projects/<slug>/finished_tasks/range_date/<start_date>/<end_date>/date_groups/<int:interval_days>', FinishedProjectTaskDateGroupListView.as_view(), name='finished_project_task_date_groups'),
    path('api/projects/<slug>/finished_tasks/start_date/<start_date>/date_groups/<int:interval_days>', FinishedProjectTaskDateGroupListView.as_view(), name='finished_project_task_date_groups'),
    path('api/projects/<slug>/finished_tasks/end_date/<end_date>/date_groups/<int:interval_days>', FinishedProjectTaskDateGroupListView.as_view(), name='finished_project_task_date_groups'),

    path('api/projects/<slug>/finished_tasks/range_date/<start_date>/<end_date>/date_groups/<int:interval_days>/count', FinishedProjectTaskDateGroupCount.as_view(), name='finished_project_task_date_groups_count'),
    path('api/projects/<slug>/finished_tasks/start_date/<start_date>/date_groups/<int:interval_days>/count', FinishedProjectTaskDateGroupCount.as_view(), name='finished_project_task_date_groups_count'),
    path('api/projects/<slug>/finished_tasks/end_date/<end_date>/date_groups/<int:interval_days>/count', FinishedProjectTaskDateGroupCount.as_view(), name='finished_project_task_date_groups_count'),

    path('api/projects/<slug>/tasks/range_date/<start_date>/<end_date>', ProjectTaskListView.as_view(), name='project_tasks'),
    path('api/projects/<slug>/tasks/start_date/<start_date>', ProjectTaskListView.as_view(), name='project_tasks'),
    path('api/projects/<slug>/tasks/end_date/<end_date>', ProjectTaskListView.as_view(), name='project_tasks'),
    
    path('api/projects/<slug>/unfinished_tasks/range_date/<start_date>/<end_date>/count', UnfinishedProjectTaskCount.as_view(), name='unfinished_project_task_count'),
    path('api/projects/<slug>/unfinished_tasks/start_date/<start_date>/count', UnfinishedProjectTaskCount.as_view(), name='unfinished_project_task_count'),
    path('api/projects/<slug>/unfinished_tasks/end_date/<end_date>/count', UnfinishedProjectTaskCount.as_view(), name='unfinished_project_task_count'),

    path('api/projects/<slug>/finished_tasks/range_date/<start_date>/<end_date>/<int:complexity_weight>/count', FinishedProjectTaskCount.as_view(), name='finished_project_task_count'),
    path('api/projects/<slug>/finished_tasks/start_date/<start_date>/<int:complexity_weight>/count', FinishedProjectTaskCount.as_view(), name='finished_project_task_count'),
    path('api/projects/<slug>/finished_tasks/end_date/<end_date>/<int:complexity_weight>/count', FinishedProjectTaskCount.as_view(), name='finished_project_task_count'),

    path('api/projects/<slug>/finished_tasks/range_date/<start_date>/<end_date>/count', FinishedProjectTaskCount.as_view(), name='finished_project_task_count'),
    path('api/projects/<slug>/finished_tasks/start_date/<start_date>/count', FinishedProjectTaskCount.as_view(), name='finished_project_task_count'),
    path('api/projects/<slug>/finished_tasks/end_date/<end_date>/count', FinishedProjectTaskCount.as_view(), name='finished_project_task_count'),

    path('api/projects/<slug>/tasks/range_date/<start_date>/<end_date>/count', ProjectTaskCount.as_view(), name='project_task_count'),
    path('api/projects/<slug>/tasks/start_date/<start_date>/count', ProjectTaskCount.as_view(), name='project_task_count'),
    path('api/projects/<slug>/tasks/end_date/<end_date>/count', ProjectTaskCount.as_view(), name='project_task_count'),
]