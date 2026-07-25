from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User , Course

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email" , "bio" , "password1" , "password2"]



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title' , "description"]
        widgets = {
            'description' : forms.Textarea(attrs={"rows" : 3}),
        }