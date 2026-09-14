from django.urls import path
from main.views import show_main, show_experience, project_list

app_name = "main"

urlpatterns = [
    path('projects/', project_list, name='project_list'),
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
]