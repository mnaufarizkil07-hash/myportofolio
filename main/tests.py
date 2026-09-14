from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from main.models import Experience

class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="AI Back-End Developer Scholar",
            description="Mempelajari teknologi AI dan pengembangan back-end pada program beasiswa teknologi digital IDCamp 2025.",
            category="part-time"
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")
        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "AI Back-End Developer Scholar")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))
        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))
        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")
        

from django.test import TestCase, Client
from django.urls import reverse
from .models import Project
from datetime import date

class ProjectTest(TestCase):
    # 1. URL dapat diakses dan menggunakan template yang tepat
    def test_project_url_and_template(self):
        response = Client().get(reverse('main:project_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_list.html')

    # 2. Tampilan kondisi ketika data masih kosong
    def test_project_list_empty_state(self):
        response = Client().get(reverse('main:project_list'))
        self.assertContains(response, "Belum ada proyek yang ditambahkan saat ini.")

    # 3. Data model muncul di halaman HTML ketika ada data
    def test_project_list_shows_data(self):
        Project.objects.create(
            title="Web Portofolio",
            description="Membangun web portofolio dengan Django.",
            date=date(2026, 9, 14),
            technology_used="Django, HTML"
        )
        response = Client().get(reverse('main:project_list'))
        self.assertContains(response, "Web Portofolio")
        self.assertContains(response, "Membangun web portofolio dengan Django.")
