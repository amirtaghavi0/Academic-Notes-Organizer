from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.urls import reverse



class User(AbstractUser):
    bio = models.TextField(blank = True , null = True)

    def __str__(self):
        return self.username


class Course(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE, related_name = "courses")
    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True , null = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

class Note(models.Model):
    course = models.ForeignKey(Course , on_delete = models.CASCADE , related_name = "notes")
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length=300, blank=True, null=True)
    content = models.TextField(blank=True, null=True, help_text="Main note text.")
    file  = models.FileField(upload_to="notes_file/" , help_text="Optional PDF, image or Word file.", blank = True , null = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
 