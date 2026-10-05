from django import forms
from .models import Project, Experience
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'date', 'technology_used']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Contoh: Web Portofolio', 'maxlength': 200}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Ceritakan proyekmu di sini...', 'rows': 4}),
            'date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'technology_used': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Teknologi yang Digunakan'}),
        }
    def clean_title(self):
        title = self.cleaned_data.get('title')
        return strip_tags(title)

    def clean_description(self):
        description = self.cleaned_data.get('description')
        return strip_tags(description)

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'category', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Contoh: COMPFEST & RISTEK UI'}),
            'category': forms.Select(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Ceritakan pengalamanmu di sini...', 'rows': 4}),
        }
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'date', 'technology_used']  # Sesuaikan dengan nama di models.py
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Judul Proyek'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Deskripsi proyek...', 'rows': 4}),
            'date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'technology_used': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Teknologi yang digunakan'}),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_technology(self):
        return strip_tags(self.cleaned_data.get("technology", "")).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data.get("description", "")).strip()