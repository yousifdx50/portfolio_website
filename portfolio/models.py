from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    CATEGORY_CHOICES = [
        ("web_dev", _("Website Development")),
        ("backend_dev", _("General Backend Development")),
        ("ml_dev", _("Machine Learning Development")),
    ]

    slug = models.SlugField(max_length=120, unique=True, help_text="A unique slug for the project.")
    title = models.CharField(max_length=120)
    title_tr = models.CharField(max_length=120, blank=True)
    title_ar = models.CharField(max_length=120, blank=True)
    description = models.TextField()
    description_tr = models.TextField(blank=True)
    description_ar = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    tech_stack = models.CharField(max_length=255)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title


class PortfolioProfile(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    headline_en = models.CharField(max_length=255, blank=True)
    headline_tr = models.CharField(max_length=255, blank=True)
    headline_ar = models.CharField(max_length=255, blank=True)

    bio_en = models.TextField(blank=True)
    bio_tr = models.TextField(blank=True)
    bio_ar = models.TextField(blank=True)

    location_en = models.CharField(max_length=120, blank=True)
    location_tr = models.CharField(max_length=120, blank=True)
    location_ar = models.CharField(max_length=120, blank=True)

    roles_en = models.TextField(blank=True, help_text="One role per line")
    roles_tr = models.TextField(blank=True, help_text="One role per line")
    roles_ar = models.TextField(blank=True, help_text="One role per line")

    skills_en = models.TextField(blank=True, help_text="One skill per line")
    skills_tr = models.TextField(blank=True, help_text="One skill per line")
    skills_ar = models.TextField(blank=True, help_text="One skill per line")

    languages_en = models.TextField(blank=True, help_text="One language per line")
    languages_tr = models.TextField(blank=True, help_text="One language per line")
    languages_ar = models.TextField(blank=True, help_text="One language per line")

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Portfolio Profile"
        verbose_name_plural = "Portfolio Profile"

    def __str__(self) -> str:
        return self.name or "Portfolio Profile"
