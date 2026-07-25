from django.urls import path
from .views import *

urlpatterns =[
    path("signup/" , signup ,name = "signup"),
    path('' , course_list , name= "course_list"),
    path('courses/create/' , course_create , name="course_create"),
    path("courses/<int:course_id>/edit" ,course_edit , name ="course_edit" ),
    path('coueses/<int>:course_id' , course_detail , name="course_detail")
]