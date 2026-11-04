from datetime import date
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from main.models import Experience, Project


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="AI Back-End Developer Scholar",
            description="Mempelajari teknologi AI dan pengembangan back-end pada program beasiswa teknologi digital IDCamp 2025.",
            category="part-time",
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
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada riwayat experience")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.experience.is_ongoing)


class ProjectTest(TestCase):
    def setUp(self):
        self.client = Client()

    # 1. URL dapat diakses dan menggunakan template yang tepat
    def test_project_url_and_template(self):
        response = self.client.get(reverse("main:project_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project_list.html")

    # 2. Tampilan kondisi container empty state tersedia di template
    def test_project_list_empty_state(self):
        response = self.client.get(reverse("main:project_list"))
        self.assertContains(response, "Belum ada proyek")

    # 3. Data model muncul melalui endpoint JSON yang dipakai oleh AJAX
    def test_project_list_shows_data(self):
        project = Project.objects.create(
            title="Web Portofolio",
            description="Membangun web portofolio dengan Django.",
            date=date(2026, 9, 14),
            technology_used="Django, HTML",
        )
        # Cek melalui endpoint JSON yang dikonsumsi oleh AJAX project_list.html
        json_response = self.client.get(reverse("main:get_projects_json"))
        self.assertEqual(json_response.status_code, 200)
        self.assertContains(json_response, "Web Portofolio")
        self.assertContains(json_response, "Membangun web portofolio dengan Django.")
        self.assertEqual(project.technology, "Django, HTML")