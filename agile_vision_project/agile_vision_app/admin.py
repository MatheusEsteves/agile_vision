from django.contrib import admin
from .models import *
from .forms import *

class IndicatorsInline(admin.TabularInline):
    model = IndicatorItem
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    inlines = [
        IndicatorsInline
    ]

class TeamAdmin(admin.ModelAdmin):
    form = TeamForm

class TaskLabelAdmin(admin.ModelAdmin):
    form = TaskLabelForm
    list_display = ['title', 'color']

admin.site.register(Member)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(IndicatorVision)
admin.site.register(IndicatorType)
admin.site.register(TaskComplexity)
admin.site.register(Task)
admin.site.register(TaskLabel, TaskLabelAdmin)