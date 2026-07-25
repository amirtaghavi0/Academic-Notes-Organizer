from django.urls import path
from .views import *

urlpatterns =[
    path("signup/" , signup ,name = "signup"),
    path('' , course_list , name= "course_list"),
    path('courses/create/' , course_create , name="course_create")
]