from django.forms import ModelForm, TextInput, Textarea, DateInput
from main.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # Ini field asli yang ada di models.py lu
        fields = ["title", "description", "date", "technology_used"]
        
        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "date": "Tanggal Proyek",
            "technology_used": "Teknologi yang Digunakan",
        }
        
        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Contoh: Web Portofolio",
                    "maxlength": 200,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan proyekmu di sini...",
                    "rows": 3,
                }
            ),
            "date": DateInput(
                attrs={
                    "type": "date", # Biar muncul kalender pas di-klik
                }
            ),
            "technology_used": TextInput(
                attrs={
                    "placeholder": "Contoh: Django, Python, HTML",
                }
            ),
        }