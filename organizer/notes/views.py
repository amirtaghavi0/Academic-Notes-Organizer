from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , get_object_or_404 , redirect
from .forms import SignUpForm , CourseForm ,NoteForm
from django.contrib.auth import login
from .models import Course , Note 
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
    return render(request , 'notes/course_list.html' , {"courses" : courses})
    
    
@login_required
def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course= form.save(commit = False)
            course.user = request.user
            course.save()
            return redirect("course_list")
    else:
        form = CourseForm()
    return render(request , "notes/course_form.html" , {"form" : form , 'mode' : "create"})



def course_edit(request, course_id):
    return render(request , "notes/course_form.html" , {"mode" : "edit"})



def course_detail(request, course_id):
    course = get_object_or_404(Course , id = course_id , user = request.user)
    notes = course.notes.all()
    return render(request , "notes/course_detail.html" , {"course" : course , "notes" : notes})
    

def course_delete(request , course_id):
    course = get_object_or_404(Course , id = course_id , user = request.user)
    if request.method == "POST":
        course.delete()
        return redirect("course_list")
    return render(request , 'notes/course_confirm_delete.html' , {"course" : course})



def note_create(request , course_id):
    course = get_object_or_404(Course , id=course_id , user = request.user)
    if request.method == "POST":
        form = NoteForm(request.POST , request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.course = course
            note.save()
            return redirect("course_detail" , course_id = course.id)
    else:
         form = NoteForm()
    return render(request , 'notes/note_form.html' , {"form" : form, "course": course , "mode" : "create"} )
    



def note_detail(request , note_id):
    note = get_object_or_404(Note , id = note_id  ,course__user = request.user)
    return render(request , 'notes/note_detail.html' , {"note": note})


def note_delete(request, note_id):
    note = get_object_or_404(Note , id = note_id , course__user=request.user)
    if request.method == "POST":
        note.delete()
        return redirect('course_detail' ,course_id=note.course.id)
    return render(request , 'notes/note_confirm_delete.html', {"note": note})


def note_edit(request, note_id):
    return render(request , 'notes/note_form.html' , {'mode' : "edit"})