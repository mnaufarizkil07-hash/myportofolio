from django.urls import path
from main.views import show_main, show_experience, project_list, create_project, get_projects_json, delete_project # <-- import baru ditambahin

app_name = "main"

urlpatterns = [
    path('projects/', project_list, name='project_list'),
    path('', show_main, name='show_main'),
    path('experience/', show_experience, name='show_experience'),
    path('create-project/', create_project, name='create_project'),
    
    # URL baru buat JSON dan Delete
    path('api/projects/', get_projects_json, name='get_projects_json'),
    path('projects/<uuid:project_id>/delete/', delete_project, name='delete_project'),
]