from django.test import TestCase, Client
from django.urls import reverse
from portfolio.models import Project, PortfolioProfile


class PortfolioViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a profile for views that depend on it
        PortfolioProfile.objects.create(name="Test User", email="test@example.com")
        # Create some projects
        Project.objects.create(
            slug="web-project",
            title="Web Project",
            description="Web dev project",
            category="web_dev",
            tech_stack="HTML, CSS",
            featured=True,
        )
        Project.objects.create(
            slug="ml-project",
            title="ML Project",
            description="Machine learning project",
            category="ml_dev",
            tech_stack="Python, PyTorch",
            featured=False,
        )

    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "portfolio/home.html")
        self.assertContains(response, "Web Project")
        self.assertNotContains(response, "ML Project") # Only featured projects on home

    def test_about_view(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "portfolio/about.html")
        self.assertContains(response, "Test User")

    def test_projects_view(self):
        response = self.client.get(reverse("projects"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "portfolio/projects.html")
        self.assertContains(response, "Web Project")
        self.assertContains(response, "ML Project") # All projects on projects page

    def test_contact_view(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "portfolio/contact.html")

    def test_home_view_localization(self):
        # Test Turkish localization
        response_tr = self.client.get(reverse("home") + "?lang=tr")
        self.assertEqual(response_tr.status_code, 200)
        self.assertContains(response_tr, "Portf\u00f6y") # Check for a Turkish translation

        # Test Arabic localization
        response_ar = self.client.get(reverse("home") + "?lang=ar")
        self.assertEqual(response_ar.status_code, 200)
        self.assertContains(response_ar, "\u0645\u0644\u0641 \u0627\u0644\u0627\u0639\u0645\u0627\u0644") # Check for an Arabic translation