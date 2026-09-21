from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    
    # Project URLs
    path('projects/', views.project_list, name='project_list'),
    path('create-project/', views.create_project, name='create_project'),
    path('projects/<int:id>/edit/', views.edit_project, name='edit_project'),
    path('projects/<int:id>/delete/', views.delete_project, name='delete_project'),
    
    # Experience URLs (Menggunakan <uuid:id> karena ID model experience berupa UUID)
    path('experience/', views.show_experience, name='show_experience'),
    path('experience/add/', views.create_experience, name='create_experience'),
    path('experience/<uuid:id>/edit/', views.edit_experience, name='edit_experience'),
    path('experience/<uuid:id>/delete/', views.delete_experience, name='delete_experience'),
    
    # JSON / API
    path('api/projects/', views.get_projects_json, name='get_projects_json'),
]