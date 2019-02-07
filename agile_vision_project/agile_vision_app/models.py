from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    mentor = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='static/images/members')
    
    class Meta:
        verbose_name = u'Member'
        verbose_name_plural = u'Members'
    
    def __str__(self):
        return self.name
