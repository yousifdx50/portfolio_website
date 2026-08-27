from django.db import migrations, models


def rename_seeded_projects(apps, schema_editor):
    Project = apps.get_model("portfolio", "Project")
    renames = {
        "automation-workflow-system": ("process-automation-engine", "Process Automation Engine"),
        "ecommerce-backend-api": ("commerce-core-api", "Commerce Core API"),
        "ml-automation-project": ("ml-automation-pipeline", "ML Automation Pipeline"),
    }
    for old_slug, (new_slug, title) in renames.items():
        Project.objects.filter(slug=old_slug).update(slug=new_slug, title=title)


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0003_project_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="architecture_image",
            field=models.CharField(
                blank=True,
                help_text="Static path for the architecture or database diagram",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="features",
            field=models.TextField(blank=True, help_text="One feature per line"),
        ),
        migrations.AddField(
            model_name="project",
            name="features_ar",
            field=models.TextField(blank=True, help_text="One feature per line"),
        ),
        migrations.AddField(
            model_name="project",
            name="features_tr",
            field=models.TextField(blank=True, help_text="One feature per line"),
        ),
        migrations.AddField(
            model_name="project",
            name="problem_statement",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="problem_statement_ar",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="problem_statement_tr",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="project",
            name="project_image",
            field=models.CharField(
                blank=True,
                help_text="Static path for the project visual",
                max_length=255,
            ),
        ),
        migrations.RunPython(rename_seeded_projects, migrations.RunPython.noop),
    ]
