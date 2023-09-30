from django.db import models
from django.contrib.auth.models import User
from datetime import date

class profile(models.Model):
    '''a model for a blog post'''

    Name = models.OneToOneField(User, on_delete=models.CASCADE)
    Phone_no = models.CharField(max_length=100)
    Email = models.TextField()

    def __str__(self):
        return self.user.Name