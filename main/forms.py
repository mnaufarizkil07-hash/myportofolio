from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

from .models import Project, Experience


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "tech_stack", "project_url", "project_image_url"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-input", "placeholder": "Contoh: Web Portofolio"}),
            "description": forms.Textarea(attrs={"class": "form-input", "placeholder": "Ceritakan proyekmu di sini...", "rows": 4}),
            "tech_stack": forms.TextInput(attrs={"class": "form-input", "placeholder": "Contoh: Django, REST Framework"}),
            "project_url": forms.URLInput(attrs={"class": "form-input", "placeholder": "https://example.com"}),
            "project_image_url": forms.URLInput(attrs={"class": "form-input", "placeholder": "https://example.com/image.png"}),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data.get("title", "")).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML atau spasi kosong.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data.get("description", "")).strip()

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data.get("tech_stack", "")).strip()


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "category", "description"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-input", "placeholder": "Contoh: COMPFEST & RISTEK UI"}),
            "category": forms.Select(attrs={"class": "form-input"}),
            "description": forms.Textarea(attrs={"class": "form-input", "placeholder": "Ceritakan pengalamanmu di sini...", "rows": 4}),
        }
