from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PortfolioProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("phone", models.CharField(blank=True, max_length=40)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("github", models.URLField(blank=True)),
                ("linkedin", models.URLField(blank=True)),
                ("headline_en", models.CharField(blank=True, max_length=255)),
                ("headline_tr", models.CharField(blank=True, max_length=255)),
                ("headline_ar", models.CharField(blank=True, max_length=255)),
                ("bio_en", models.TextField(blank=True)),
                ("bio_tr", models.TextField(blank=True)),
                ("bio_ar", models.TextField(blank=True)),
                ("location_en", models.CharField(blank=True, max_length=120)),
                ("location_tr", models.CharField(blank=True, max_length=120)),
                ("location_ar", models.CharField(blank=True, max_length=120)),
                ("roles_en", models.TextField(blank=True, help_text="One role per line")),
                ("roles_tr", models.TextField(blank=True, help_text="One role per line")),
                ("roles_ar", models.TextField(blank=True, help_text="One role per line")),
                ("skills_en", models.TextField(blank=True, help_text="One skill per line")),
                ("skills_tr", models.TextField(blank=True, help_text="One skill per line")),
                ("skills_ar", models.TextField(blank=True, help_text="One skill per line")),
                ("languages_en", models.TextField(blank=True, help_text="One language per line")),
                ("languages_tr", models.TextField(blank=True, help_text="One language per line")),
                ("languages_ar", models.TextField(blank=True, help_text="One language per line")),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Portfolio Profile",
                "verbose_name_plural": "Portfolio Profile",
            },
        ),
    ]
