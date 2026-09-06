from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from portfolio import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("projects/", views.projects, name="projects"),
    path("projects/<slug:slug>/", views.project_detail, name="project_detail"),
    path("contact/", views.contact, name="contact"),
    path("robots.txt", views.robots_txt, name="robots"),
    path("sitemap.xml", views.sitemap_xml, name="sitemap"),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
