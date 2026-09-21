from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from .models import Project, Experience
from .forms import ProjectForm, ExperienceForm

def show_main(request):
    context = {
        'nama': 'Muhammad Naufal Rizki Fadhlurrahman',
        'npm': '2506623490',
        'study_program': 'S1 Sistem Informasi',
        'bio': 'Mahasiswa Fakultas Ilmu Komputer Universitas Indonesia yang tertarik pada bidang cybersecurity (blue team) dan pengembangan back-end AI.'
    }
    return render(request, 'index.html', context)

# --- PROJECT VIEWS (CRUD & JSON) ---

def project_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_list.html', context)

def create_project(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('main:project_list')
    return render(request, 'create_project.html', {'form': form})

def edit_project(request, id):
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('main:project_list')
    return render(request, 'create_project.html', {'form': form})

def delete_project(request, id):
    project = get_object_or_404(Project, pk=id)
    project.delete()
    return redirect('main:project_list')

def get_projects_json(request):
    data = Project.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


# --- EXPERIENCE VIEWS (CRUD LENGKAP) ---

def show_experience(request):
    experiences = Experience.objects.all()
    context = {
        'experiences': experiences
    }
    return render(request, 'experience.html', context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('main:show_experience')
    return render(request, 'create_experience.html', {'form': form})

def edit_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if form.is_valid():
        form.save()
        return redirect('main:show_experience')
    return render(request, 'create_experience.html', {'form': form})

def delete_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    experience.delete()
    return redirect('main:show_experience')