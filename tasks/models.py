from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField()
    assigned_to = models.ForeignKey(User, related_name="tasks", on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=[('todo', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')], default='todo')

    def __str__(self):
        return self.title
