from django.conf import settings
from django.db import models

from common.models import TimeStampedModel


class Task(TimeStampedModel):

    class Status(models.TextChoices):
        TODO = "TODO", "To Do"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        DONE = "DONE", "Done"

    title = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    status = models.CharField(max_length=20,choices=Status.choices,default=Status.TODO)

    project = models.ForeignKey("projects.Project",on_delete=models.CASCADE,related_name="tasks")

    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,related_name="assigned_tasks")

    def __str__(self):
        return self.title
    
    
class Comment(TimeStampedModel):

    content = models.TextField()

    task = models.ForeignKey(Task,on_delete=models.CASCADE,related_name="comments")

    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="comments")

    def __str__(self):
        return f"{self.author} comment"