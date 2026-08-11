from django.contrib import admin

from .models import PortfolioProfile, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "title_tr", "title_ar", "category", "featured", "created_at")
    list_filter = ("category", "featured")
    search_fields = (
        "title",
        "title_tr",
        "title_ar",
        "description",
        "description_tr",
        "description_ar",
        "tech_stack",
    )


@admin.register(PortfolioProfile)
class PortfolioProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "updated_at")

    fieldsets = (
        (
            "Core",
            {
                "fields": ("name", "phone", "email", "github", "linkedin"),
            },
        ),
        (
            "English",
            {
                "fields": (
                    "headline_en",
                    "bio_en",
                    "location_en",
                    "roles_en",
                    "skills_en",
                    "languages_en",
                )
            },
        ),
        (
            "Turkish",
            {
                "fields": (
                    "headline_tr",
                    "bio_tr",
                    "location_tr",
                    "roles_tr",
                    "skills_tr",
                    "languages_tr",
                )
            },
        ),
        (
            "Arabic",
            {
                "fields": (
                    "headline_ar",
                    "bio_ar",
                    "location_ar",
                    "roles_ar",
                    "skills_ar",
                    "languages_ar",
                )
            },
        ),
    )
