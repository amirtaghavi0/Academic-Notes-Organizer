from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , get_object_or_404 , redirect
from .forms import SignUpForm
from django.contrib.auth import login
from .models import Course
# Create your views here.


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect("course_list")

    else:
        form = SignUpForm()
    return render(request , "registration/signup.html" , {"form" : form})


@login_required
def course_list(request):
    courses = Course.objects.filter(user = request.user).prefetch_related("notes")
    return render(request , 'notes/course_list.html' , {"course" : courses})
    
    
@login_required
def course_create(request):
    pass