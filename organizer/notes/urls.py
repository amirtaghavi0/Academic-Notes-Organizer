from django.urls import path
from .views import *

urlpatterns =[
    path("signup/" , signup ,name = "signup"),
    path('' , course_list , name= "course_list"),
    path('courses/create/' , course_create , name="course_create"),
    path("courses/<int:course_id>/edit" ,course_edit , name ="course_edit" ),
    path('coueses/<int:course_id>/' , course_detail , name="course_detail"),
    path('courses/<int:course_id>/delete/' , course_delete , name= "course_delete"),
    path('courses/<int:course_id>/notes/create/' , note_create , name= "note_create"),
    path('notes/<int:note_id>/' , note_detail , name="note_detail"),
    path('notes/<int:note_id>/edit/' , note_edit , name="note_edit"),
    path('notes/<int:note_id>/delete/' , note_delete , name="note_delete"),
    
]