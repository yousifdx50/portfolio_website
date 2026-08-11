from django.test import TestCase
from portfolio.models import Project, PortfolioProfile


class ProjectModelTest(TestCase):
    def setUp(self):
        self.project_data = {
            "title": "Test Project",
            "description": "A description for the test project.",
            "category": "web_dev",
            "tech_stack": "Python, Django, HTML, CSS",
            "github_url": "https://github.com/test/project",
            "live_url": "https://testproject.com",
            "featured": True,
        }
        self.project = Project.objects.create(**self.project_data)

    def test_project_creation(self):
        self.assertEqual(self.project.title, "Test Project")
        self.assertEqual(self.project.category, "web_dev")
        self.assertTrue(self.project.featured)
        self.assertIsNotNone(self.project.created_at)

    def test_project_str_representation(self):
        self.assertEqual(str(self.project), "Test Project")

    def test_localized_fields(self):
        self.project.title_tr = "Test Projesi"
        self.project.description_ar = "وصف المشروع التجريبي"
        self.project.save()
        self.assertEqual(self.project.title_tr, "Test Projesi")
        self.assertEqual(self.project.description_ar, "وصف المشروع التجريبي")


class PortfolioProfileModelTest(TestCase):
    def test_profile_creation_and_singleton(self):
        # Create the first profile
        profile1 = PortfolioProfile.objects.create(name="Yousif", email="yousif@example.com")
        self.assertEqual(profile1.pk, 1)
        self.assertEqual(profile1.name, "Yousif")

        # Try to create a second profile, it should overwrite the first one due to save() method
        profile2 = PortfolioProfile.objects.create(name="New Name", email="new@example.com")
        self.assertEqual(profile2.pk, 1) # Still PK 1
        self.assertEqual(profile2.name, "New Name")

        # Verify only one profile exists and it's the updated one
        self.assertEqual(PortfolioProfile.objects.count(), 1)
        self.assertEqual(PortfolioProfile.objects.first().name, "New Name")