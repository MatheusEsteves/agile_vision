from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import *

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = []

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        self.fields['members'] = forms.ModelMultipleChoiceField(
            queryset=Member.objects.all(),
            label='Members',
            widget=FilteredSelectMultiple(verbose_name='Members', is_stacked=False)
        )

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        exclude = []

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)

        self.fields['projects'] = forms.ModelMultipleChoiceField(
            queryset=Project.objects.all(),
            label='Projects',
            widget=FilteredSelectMultiple(verbose_name='Projects', is_stacked=False)
        )