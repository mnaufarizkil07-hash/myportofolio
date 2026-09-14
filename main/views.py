from django.shortcuts import render
from main.models import Experience, Project

def show_main(request):
    context = {
        "name": "Muhammad Naufal Rizki Fadhlurrahman",
        "npm": "2506623490",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Fakultas Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada bidang cybersecurity (blue team) dan pengembangan back-end AI."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Muhammad Naufal Rizki Fadhlurrahman",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def project_list(request):
    context = {
        "project_list": Project.objects.all()
    }
    return render(request, "project_list.html", context)