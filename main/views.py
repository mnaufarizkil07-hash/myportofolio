from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from .models import Project, Experience
from .forms import ProjectForm, ExperienceForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.views.decorators.http import require_ZPOST, require_POST
from django.http import JsonResponse
from main.forms import ProjectForm

def is_editor_or_superuser(user):
    return user.is_superuser or user.groups.filter(name='Editor').exists()

def show_main(request):
    title_query = request.GET.get("title", "").strip()
    
    context = {
        'nama': 'Muhammad Naufal Rizki Fadhilurrahman',
        'npm': '2506623490',
        'study_program': 'S1 Sistem Informasi',
        'bio': 'Mahasiswa Fakultas Ilmu Komputer Universitas Indonesia',
        'last_login': request.COOKIES.get('last_login'),
        'title_query': title_query,
        'form': ProjectForm(),
    }
    return render(request, 'project_list.html', context)

# --- PROJECT VIEWS (CRUD & JSON) ---

def project_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_list.html', context)

@login_required(login_url='/login/')
def create_project(request):
    if not is_editor_or_superuser(request.user):
        return HttpResponseForbidden("Anda tidak memiliki izin untuk menambah proyek.")
    
    form = ProjectForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_project.html", context)

@login_required(login_url='/login/')
def edit_project(request, id):
    if not is_editor_or_superuser(request.user):
        return HttpResponseForbidden("Anda tidak memiliki izin untuk mengubah proyek ini.")

    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form, 'project': project}
    return render(request, "edit_project.html", context)

@login_required(login_url='/login/')
def delete_project(request, id):
    # HANYA Superuser (Pemilik Portofolio) yang boleh menghapus
    if not request.user.is_superuser:
        return HttpResponseForbidden("Hanya pemilik portofolio yang dapat menghapus proyek.")

    project = get_object_or_404(Project, pk=id)
    project.delete()
    return redirect('main:show_main')
def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()
    
    if title_query:
        projects = projects.filter(title__icontains=title_query)
        
    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])
        
        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })
        
    return JsonResponse(data, safe=False)


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

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")
    
    context = {
        "name": "Naufal Rizki",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        # Membuat response untuk memasang cookie last_login
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
        
    context = {
        "name": "Naufal Rizki",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect("main:show_main")

@login_required(login_url='main:login')
def toggle_star(request, id):
    # Ambil data proyek berdasarkan ID-nya
    project = get_object_or_404(Project, pk=id)
    
    # Cek apakah user yang sedang login sudah pernah nge-star proyek ini
    if request.user in project.stars.all():
        project.stars.remove(request.user) # Kalau sudah, cabut bintangnya (Unlike)
    else:
        project.stars.add(request.user) # Kalau belum, tambahkan bintangnya (Like)
        
    # Kembalikan user ke halaman utama setelah klik
    return redirect('main:show_main')

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403
        )
    
    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse({
            "message": "Proyek berhasil ditambahkan.",
            "pk": str(project.id)
        }, status=201)
    
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)