from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    bio = models.TextField(blank = True , null = True)


class Course(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE, related_name = "courses")
    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True , null = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    

class Note(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE , related_name ="user_notes")
    course = models.ForeignKey(Course , on_delete = models.CASCADE , related_name = "notes")
    title = models.CharField(max_length = 200)
    file  = models.FileField(upload_to="notes_file/")
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title