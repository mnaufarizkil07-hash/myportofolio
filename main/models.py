import uuid
from django.db import models
from django.contrib.auth.models import User


class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ("internship", "Internship"),
        ("research", "Research"),
        ("volunteer", "Volunteer"),
        ("part-time", "Part-Time"),
        ("full-time", "Full-Time"),
        ("freelance", "Freelance"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=20, choices=EXPERIENCE_CHOICES, default="full-time"
    )
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def is_ongoing(self):
        return self.ended_at is None


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=100, blank=True, default="")
    project_url = models.URLField(blank=True, default="")
    project_image_url = models.URLField(blank=True, default="")
    starred_by = models.ManyToManyField(User, related_name="starred_projects", blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __init__(self, *args, **kwargs):
        if "technology_used" in kwargs and "tech_stack" not in kwargs:
            kwargs["tech_stack"] = kwargs.pop("technology_used")
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def technology(self):
        return self.tech_stack

    @property
    def technology_used(self):
        return self.tech_stack

    @technology_used.setter
    def technology_used(self, value):
        self.tech_stack = value

    @property
    def stars(self):
        return self.starred_by

    @property
    def star_count(self):
        return self.starred_by.count()