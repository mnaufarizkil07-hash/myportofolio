from django.contrib import messages # Tambahin ini di deretan import paling atas ya!

# ... (kode view lainnya) ...

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        # Ini buat nampilin pesan sukses pas data berhasil disimpen
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:project_list") 

    context = {
        "name": "Naufal", # Ganti pakai nama lu
        "form": form,
    }
    return render(request, "create_project.html", context)