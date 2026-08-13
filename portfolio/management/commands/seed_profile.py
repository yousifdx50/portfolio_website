﻿import os
from django.core.management.base import BaseCommand

from portfolio.models import PortfolioProfile


class Command(BaseCommand):
    help = "Creates or updates a default multilingual portfolio profile"

    def handle(self, *args, **options):
        profile, created = PortfolioProfile.objects.update_or_create(
            id=1,
            defaults={
                "name": os.environ.get("PORTFOLIO_NAME", "Yousif Hayder Alzubaidi"),
                "phone": os.environ.get("PORTFOLIO_PHONE", "+90 531 268 1181"),
                "email": os.environ.get("PORTFOLIO_EMAIL", "yousifdx9@gmail.com"),
                "github": os.environ.get("PORTFOLIO_GITHUB", "https://github.com/yousifdx50"),
                "linkedin": os.environ.get("PORTFOLIO_LINKEDIN", "https://linkedin.com/in/yousif-hayder-ab8827319"),
                "headline_en": "Software Engineering Student | Website Developer | Backend Developer | ML Developer",
                "headline_tr": (
                    "Yazilim Muhendisligi Ogrencisi | Web Gelistirici | Backend Gelistirici | ML Gelistirici"
                ),
                "headline_ar": "طالب هندسة البرمجيات | مطور ويب | مطور باك اند | مطور تعلم الآلة",
                "bio_en": (
                    "Backend-focused Software Engineering senior at Ostim Technical University with a strong "
                    "foundation in Java, Python, and C++. Passionate about scalable backend systems, RESTful "
                    "API design, and enterprise-level architecture."
                ),
                "bio_tr": (
                    "Ostim Technical University'de 4. sinif Yazilim Muhendisligi ogrencisiyim. Java, Python "
                    "ve C++ alanlarinda guclu bir temelim var. Olceklenebilir backend sistemleri ve REST API "
                    "gelistirmeye odaklaniyorum."
                ),
                "bio_ar": (
                    "أنا طالب هندسة برمجيات في السنة الرابعة في Ostim Technical University. "
                    "لدي أساس قوي في Java وPython وC++. "
                    "أركز على بناء أنظمة Backend قابلة للتوسع وتصميم REST APIs."
                ),
                "location_en": "Ankara, Turkiye",
                "location_tr": "Ankara, Turkiye",
                "location_ar": "أنقرة، تركيا",
                "roles_en": "Website Developer\nGeneral Backend Developer\nMachine Learning Developer",
                "roles_tr": "Web Gelistirici\nGenel Backend Gelistirici\nMakine Ogrenmesi Gelistirici",
                "roles_ar": "مطور مواقع ويب\nمطور باك اند عام\nمطور تعلم الآلة",
                "skills_en": (
                    "Java\nPostgreSQL\nSpring Boot\nFastAPI\nFlask\nExpress.js\nNode.js\nREST APIs\nPython\n"
                    "C++\nSQL\nDocker\nLinux (Ubuntu/Debian)\nGit/GitHub\nPyTorch\nNumPy\nPandas\nMatplotlib"
                ),
                "skills_tr": (
                    "Java\nPostgreSQL\nSpring Boot\nFastAPI\nFlask\nExpress.js\nNode.js\nREST APIs\nPython\n"
                    "C++\nSQL\nDocker\nLinux (Ubuntu/Debian)\nGit/GitHub\nPyTorch\nNumPy\nPandas\nMatplotlib"
                ),
                "skills_ar": (
                    "Java\nPostgreSQL\nSpring Boot\nFastAPI\nFlask\nExpress.js\nNode.js\nREST APIs\nPython\n"
                    "C++\nSQL\nDocker\nLinux (Ubuntu/Debian)\nGit/GitHub\nPyTorch\nNumPy\nPandas\nMatplotlib"
                ),
                "languages_en": "Arabic (Native)\nEnglish (Advanced - C1)\nTurkish (Upper Intermediate - B2)",
                "languages_tr": "Arapca (Ana dil)\nIngilizce (Ileri seviye - C1)\nTurkce (Ust orta seviye - B2)",
                "languages_ar": "العربية (اللغة الأم)\nالإنجليزية (متقدم - C1)\nالتركية (فوق المتوسط - B2)",
            },
        )

        if created:
            self.stdout.write(self.style.SUCCESS("Default multilingual profile created."))
        else:
            self.stdout.write(self.style.SUCCESS("Default profile updated."))
