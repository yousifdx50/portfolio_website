from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=120)),
                ("title_tr", models.CharField(blank=True, max_length=120)),
                ("title_ar", models.CharField(blank=True, max_length=120)),
                ("description", models.TextField()),
                ("description_tr", models.TextField(blank=True)),
                ("description_ar", models.TextField(blank=True)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("web_dev", "Website Development"),
                            ("backend_dev", "General Backend Development"),
                            ("ml_dev", "Machine Learning Development"),
                        ],
                        max_length=20,
                    ),
                ),
                ("tech_stack", models.CharField(max_length=255)),
                ("github_url", models.URLField(blank=True)),
                ("live_url", models.URLField(blank=True)),
                ("featured", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
