from django import forms
from .models import Project, Experience

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

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'category', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Contoh: COMPFEST & RISTEK UI'}),
            'category': forms.Select(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Ceritakan pengalamanmu di sini...', 'rows': 4}),
        }