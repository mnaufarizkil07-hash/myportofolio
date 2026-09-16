from django.shortcuts import render
from main.models import Experience, Project
from django.shortcuts import render, redirect
from main.forms import ProjectForm
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404 
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
    # Mengambil data dari fungsi JSON di atas
    json_response = get_projects_json(request)
    
    # Mengubah kembali JSON jadi objek Python (Deserialization)
    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Naufal", 
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project_list.html", context)

def create_project(request):
    # Jika pengguna menekan tombol "Submit"
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save() # Simpan data ke database
            return redirect('main:project_list') # Balik ke halaman daftar proyek
    # Jika pengguna baru buka halaman form-nya aja (GET)
    else:
        form = ProjectForm()

    context = {'form': form}
    return render(request, "create_project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()
    
    # Kalau ada pencarian (filter) by title
    if title_query:
        projects = projects.filter(title__icontains=title_query)
        
    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:project_list")
        
    return redirect("main:project_list")