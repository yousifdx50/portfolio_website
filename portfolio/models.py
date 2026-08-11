from django.db import models


class Project(models.Model):
    CATEGORY_CHOICES = [
        ("web_dev", "Website Development"),
        ("backend_dev", "General Backend Development"),
        ("ml_dev", "Machine Learning Development"),
    ]

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

    def save(self, *args, **kwargs):
        self.pk = 1  # Force the primary key to always be 1

        # `QuerySet.create()` calls `save(force_insert=True)`, which breaks the
        # singleton behavior after the first row exists. We intentionally ignore
        # `force_insert` and update the existing singleton instead.
        kwargs.pop("force_insert", None)
        if self.__class__.objects.filter(pk=1).exists():
            kwargs["force_update"] = True

        super().save(*args, **kwargs)
