from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    # Halaman Utama (Profil)
    path("", views.show_main, name="show_main"),

    # Project URLs (CRUD & Star)
    path("projects/", views.project_list, name="project_list"),
    path("create-project/", views.create_project, name="create_project"),
    path("projects/<str:id>/edit/", views.edit_project, name="edit_project"),
    path("projects/<str:id>/delete/", views.delete_project, name="delete_project"),
    path("projects/<str:id>/star/", views.toggle_star, name="toggle_star"),

    # Experience URLs (Menggunakan UUID)
    path("experience/", views.show_experience, name="show_experience"),
    path("experience/add/", views.create_experience, name="create_experience"),
    path("experience/<uuid:id>/edit/", views.edit_experience, name="edit_experience"),
    path("experience/<uuid:id>/delete/", views.delete_experience, name="delete_experience"),

    # JSON & AJAX Endpoints
    path("json/projects/", views.get_projects_json, name="get_projects_json"),
    path("api/projects/", views.get_projects_json, name="api_projects_json"),
    path("add-ajax/", views.add_project_ajax, name="add_project_ajax"),
    path("create-project-ajax/", views.create_project_ajax, name="create_project_ajax"),

    # Authentication URLs (Mendukung pemanggilan 'logout' maupun 'logout_user')
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("logout-user/", views.logout_user, name="logout_user"),
]