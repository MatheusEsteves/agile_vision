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
    path('api/projects/<slug>/tasks', ProjectTaskListView.as_view(), name='project_tasks'),
]