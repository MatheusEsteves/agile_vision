from django.db import models
from colorfield.fields import ColorField

class Member(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)
    role = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, null=True)
    mentor = models.CharField(max_length=50, null=True)
    photo = models.ImageField(upload_to='static/images/members', null=True)
    next_vacation_start_date = models.DateField(null=True)
    next_vacation_end_date = models.DateField(null=True)
    last_one_one_meeting_date = models.DateField(null=True)
    last_one_one_meeting_manager = models.CharField(max_length=50, null=True)
    
    class Meta:
        verbose_name = u'Member'
        verbose_name_plural = u'Members'
    
    def __str__(self):
        return self.name

class IndicatorVision(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()

    class Meta:
        verbose_name = u'Indicator Vision'
        verbose_name_plural = u'Indicator Visions'

    def __str__(self):
        return self.name

class IndicatorType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = u'Indicator Type'
        verbose_name_plural = u'Indicator Types'
    
    def __str__(self):
        return self.name

class Project(models.Model):
    slug = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    client = models.CharField(max_length=50)
    members = models.ManyToManyField(Member, related_name='projects', blank=True)

    class Meta:
        verbose_name = u'Project'
        verbose_name_plural = u'Projects'

    def __str__(self):
        return self.name

class IndicatorItem(models.Model):
    project = models.ForeignKey(Project, related_name='indicators', on_delete=models.CASCADE)
    indicator_type = models.ForeignKey('IndicatorType', related_name='indicators', on_delete=models.CASCADE, null=True)
    indicator_vision_currently_month = models.ForeignKey('IndicatorVision', related_name='currently_month_indicator_items', on_delete=models.CASCADE, null=True)
    indicator_vision_next_month = models.ForeignKey('IndicatorVision', related_name='next_month_indicator_items', on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = u'Project Indicator Item'
        verbose_name_plural = u'Project Indicator Items'
    
    def __str__(self):
        return str(self.indicator_type)

class Team(models.Model):
    slug = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    email = models.EmailField(null=True)
    photo = models.ImageField(upload_to='static/images/teams')
    projects = models.ManyToManyField(Project, related_name='teams', blank=True)

    class Meta:
        verbose_name = u'Team'
        verbose_name_plural = u'Teams'

    def __str__(self):
        return self.name
    
class TaskComplexity(models.Model):
    name = models.CharField(max_length=50)
    weight = models.IntegerField()

    class Meta:
        verbose_name = u'Task Complexity'
        verbose_name_plural = u'Task Complexities'

    def __str__(self):
        return self.name

class TaskLabel(models.Model):
    title = models.CharField(max_length=30, null=True)
    color = ColorField(null=True)

    class Meta:
        verbose_name = u'Task Label'
        verbose_name_plural = u'Task Labels'

    def __str__(self):
        return self.title

class Task(models.Model):
    project = models.ForeignKey('Project', related_name='tasks', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    labels = models.ManyToManyField(TaskLabel, related_name='tasks', blank=True)
    delivery_date = models.DateField(max_length=30, null=True)
    development_time = models.IntegerField(null=True, blank=True)
    validation_time = models.IntegerField(null=True, blank=True)
    blocking_time = models.IntegerField(null=True, blank=True)
    complexity = models.ForeignKey('TaskComplexity', related_name='complexity_tasks', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = u'Task'
        verbose_name_plural = u'Tasks'

    def __str__(self):
        return str(self.project) + ', ' + str(self.complexity)