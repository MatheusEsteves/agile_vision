from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = u'User'
        verbose_name_plural = u'Users'

    def __str__(self):
        return self.name
