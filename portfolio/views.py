from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import PortfolioProfile, Project

PROFILE_BASE = {
    "name": "Yousif Hayder Alzubaidi",
    "location": "Ankara, Turkiye",
    "phone": "+90 531 268 1181",
    "email": "yousifdx9@gmail.com",
    "github": "https://github.com/yousifdx50",
    "linkedin": "https://linkedin.com/in/yousif-hayder-ab8827319",
    "skills": [
        "Java",
        "PostgreSQL",
        "Spring Boot",
        "FastAPI",
        "Flask",
        "Express.js",
        "Node.js",
        "REST APIs",
        "Python",
        "C++",
        "SQL",
        "Docker",
        "Linux (Ubuntu/Debian)",
        "Git/GitHub",
        "PyTorch",
        "NumPy",
        "Pandas",
        "Matplotlib",
    ],
    "languages": [
        "Arabic (Native)",
        "English (Advanced - C1)",
        "Turkish (Upper Intermediate - B2)",
    ],
}

PROFILE_LOCALIZED = {
    "en": {
        "headline": "Software Engineering Student | Website Developer | Backend Developer | ML Developer",
        "bio": (
            "Backend-focused Software Engineering senior at Ostim Technical University with a strong "
            "foundation in Java, Python, and C++. Passionate about scalable backend systems, RESTful API "
            "design, and enterprise-level architecture."
        ),
        "roles": [
            "Website Developer",
            "General Backend Developer",
            "Machine Learning Developer",
        ],
    },
    "tr": {
        "headline": (
            "Yaz\u0131l\u0131m M\u00fchendisli\u011fi \u00d6\u011frencisi | "
            "Web Geli\u015ftirici | Backend Geli\u015ftirici | ML Geli\u015ftirici"
        ),
        "bio": (
            "Ostim Technical University'de 4. s\u0131n\u0131f Yaz\u0131l\u0131m M\u00fchendisli\u011fi "
            "\u00f6\u011frencisiyim. Java, Python ve C++ alanlar\u0131nda g\u00fc\u00e7l\u00fc bir temelim var. "
            "\u00d6l\u00e7eklenebilir backend sistemleri ve REST API geli\u015ftirmeye odaklan\u0131yorum."
        ),
        "location": "Ankara, T\u00fcrkiye",
        "languages": [
            "Arap\u00e7a (Ana dil)",
            "\u0130ngilizce (\u0130leri seviye - C1)",
            "T\u00fcrk\u00e7e (\u00dcst orta seviye - B2)",
        ],
        "roles": [
            "Web Geli\u015ftirici",
            "Genel Backend Geli\u015ftirici",
            "Makine \u00d6\u011frenmesi Geli\u015ftirici",
        ],
    },
    "ar": {
        "headline": (
            "\u0637\u0627\u0644\u0628 \u0647\u0646\u062f\u0633\u0629 \u0627\u0644\u0628\u0631\u0645\u062c\u064a\u0627\u062a | "
            "\u0645\u0637\u0648\u0631 \u0648\u064a\u0628 | "
            "\u0645\u0637\u0648\u0631 \u0628\u0627\u0643 \u0627\u0646\u062f | "
            "\u0645\u0637\u0648\u0631 \u062a\u0639\u0644\u0645 \u0627\u0644\u0622\u0644\u0629"
        ),
        "bio": (
            "\u0623\u0646\u0627 \u0637\u0627\u0644\u0628 \u0647\u0646\u062f\u0633\u0629 \u0628\u0631\u0645\u062c\u064a\u0627\u062a "
            "\u0641\u064a \u0627\u0644\u0633\u0646\u0629 \u0627\u0644\u0631\u0627\u0628\u0639\u0629 \u0641\u064a Ostim Technical University. "
            "\u0644\u062f\u064a \u0623\u0633\u0627\u0633 \u0642\u0648\u064a \u0641\u064a Java \u0648Python \u0648C++. "
            "\u0623\u0631\u0643\u0632 \u0639\u0644\u0649 \u0628\u0646\u0627\u0621 \u0623\u0646\u0638\u0645\u0629 Backend "
            "\u0642\u0627\u0628\u0644\u0629 \u0644\u0644\u062a\u0648\u0633\u0639 \u0648\u062a\u0635\u0645\u064a\u0645 REST APIs."
        ),
        "location": "\u0623\u0646\u0642\u0631\u0629\u060c \u062a\u0631\u0643\u064a\u0627",
        "languages": [
            "\u0627\u0644\u0639\u0631\u0628\u064a\u0629 (\u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0623\u0645)",
            "\u0627\u0644\u0625\u0646\u062c\u0644\u064a\u0632\u064a\u0629 (\u0645\u062a\u0642\u062f\u0645 - C1)",
            "\u0627\u0644\u062a\u0631\u0643\u064a\u0629 (\u0641\u0648\u0642 \u0627\u0644\u0645\u062a\u0648\u0633\u0637 - B2)",
        ],
        "roles": [
            "\u0645\u0637\u0648\u0631 \u0645\u0648\u0627\u0642\u0639 \u0648\u064a\u0628",
            "\u0645\u0637\u0648\u0631 \u0628\u0627\u0643 \u0627\u0646\u062f \u0639\u0627\u0645",
            "\u0645\u0637\u0648\u0631 \u062a\u0639\u0644\u0645 \u0627\u0644\u0622\u0644\u0629",
        ],
    },
}

TRANSLATIONS = {
    "en": {
        "site_title": "Portfolio",
        "about": "About",
        "projects": "Projects",
        "contact": "Contact",
        "about_me": "About Me",
        "location": "Location",
        "core_roles": "Core Roles",
        "skills": "Skills",
        "languages": "Languages",
        "featured_projects": "Featured Projects",
        "track": "Track",
        "stack": "Stack",
        "category": "Category",
        "tech_stack": "Tech Stack",
        "no_projects": "No projects yet.",
        "no_featured_projects": "No projects yet. Add from admin or run seed command.",
        "contact_intro": "If you want to work with me on web, backend, or ML products, reach out.",
        "phone": "Phone",
        "email": "Email",
        "github": "GitHub",
        "linkedin": "LinkedIn",
    },
    "tr": {
        "site_title": "Portf\u00f6y",
        "about": "Hakk\u0131mda",
        "projects": "Projeler",
        "contact": "\u0130leti\u015fim",
        "about_me": "Hakk\u0131mda",
        "location": "Konum",
        "core_roles": "Temel Roller",
        "skills": "Yetenekler",
        "languages": "Diller",
        "featured_projects": "\u00d6ne \u00c7\u0131kan Projeler",
        "track": "Alan",
        "stack": "Teknoloji",
        "category": "Kategori",
        "tech_stack": "Teknoloji Y\u0131\u011f\u0131n\u0131",
        "no_projects": "Hen\u00fcz proje yok.",
        "no_featured_projects": (
            "Hen\u00fcz proje yok. Admin panelinden proje ekleyebilir veya seed komutunu "
            "\u00e7al\u0131\u015ft\u0131rabilirsiniz."
        ),
        "contact_intro": "Web, backend veya ML projeleri i\u00e7in benimle ileti\u015fime ge\u00e7ebilirsiniz.",
        "phone": "Telefon",
        "email": "E-posta",
        "github": "GitHub",
        "linkedin": "LinkedIn",
    },
    "ar": {
        "site_title": "\u0645\u0644\u0641 \u0627\u0644\u0627\u0639\u0645\u0627\u0644",
        "about": "\u0646\u0628\u0630\u0629",
        "projects": "\u0627\u0644\u0645\u0634\u0627\u0631\u064a\u0639",
        "contact": "\u0627\u0644\u062a\u0648\u0627\u0635\u0644",
        "about_me": "\u0646\u0628\u0630\u0629 \u0639\u0646\u064a",
        "location": "\u0627\u0644\u0645\u0648\u0642\u0639",
        "core_roles": "\u0627\u0644\u0627\u062f\u0648\u0627\u0631 \u0627\u0644\u0627\u0633\u0627\u0633\u064a\u0629",
        "skills": "\u0627\u0644\u0645\u0647\u0627\u0631\u0627\u062a",
        "languages": "\u0627\u0644\u0644\u063a\u0627\u062a",
        "featured_projects": "\u0627\u0644\u0645\u0634\u0627\u0631\u064a\u0639 \u0627\u0644\u0645\u0645\u064a\u0632\u0629",
        "track": "\u0627\u0644\u0645\u062c\u0627\u0644",
        "stack": "\u0627\u0644\u062a\u0642\u0646\u064a\u0627\u062a",
        "category": "\u0627\u0644\u062a\u0635\u0646\u064a\u0641",
        "tech_stack": "\u0627\u0644\u0645\u0643\u062f\u0633 \u0627\u0644\u062a\u0642\u0646\u064a",
        "no_projects": "\u0644\u0627 \u062a\u0648\u062c\u062f \u0645\u0634\u0627\u0631\u064a\u0639 \u0628\u0639\u062f.",
        "no_featured_projects": (
            "\u0644\u0627 \u062a\u0648\u062c\u062f \u0645\u0634\u0627\u0631\u064a\u0639 \u0628\u0639\u062f. "
            "\u0623\u0636\u0641 \u0645\u0634\u0627\u0631\u064a\u0639 \u0645\u0646 \u0644\u0648\u062d\u0629 "
            "\u0627\u0644\u0625\u062f\u0627\u0631\u0629 \u0623\u0648 \u0634\u063a\u0644 \u0623\u0645\u0631 seed."
        ),
        "contact_intro": (
            "\u0625\u0630\u0627 \u0623\u0631\u062f\u062a \u0627\u0644\u0639\u0645\u0644 \u0645\u0639\u064a \u0641\u064a \u0645\u0634\u0627\u0631\u064a\u0639 "
            "\u0627\u0644\u0648\u064a\u0628 \u0623\u0648 Backend \u0623\u0648 ML\u060c \u062a\u0648\u0627\u0635\u0644 \u0645\u0639\u064a."
        ),
        "phone": "\u0627\u0644\u0647\u0627\u062a\u0641",
        "email": "\u0627\u0644\u0628\u0631\u064a\u062f \u0627\u0644\u0627\u0644\u0643\u062a\u0631\u0648\u0646\u064a",
        "github": "GitHub",
        "linkedin": "LinkedIn",
    },
}

SUPPORTED_LANGS = ("en", "tr", "ar")

CATEGORY_LABELS = {
    "en": {
        "web_dev": "Website Development",
        "backend_dev": "General Backend Development",
        "ml_dev": "Machine Learning Development",
    },
    "tr": {
        "web_dev": "Web Geli\u015ftirme",
        "backend_dev": "Genel Backend Geli\u015ftirme",
        "ml_dev": "Makine \u00d6\u011frenmesi Geli\u015ftirme",
    },
    "ar": {
        "web_dev": "\u062a\u0637\u0648\u064a\u0631 \u0645\u0648\u0627\u0642\u0639 \u0627\u0644\u0648\u064a\u0628",
        "backend_dev": "\u062a\u0637\u0648\u064a\u0631 \u0627\u0646\u0638\u0645\u0629 Backend \u0639\u0627\u0645",
        "ml_dev": "\u062a\u0637\u0648\u064a\u0631 \u062d\u0644\u0648\u0644 \u062a\u0639\u0644\u0645 \u0627\u0644\u0627\u0644\u0629",
    },
}

# Default profile for API compatibility.
PROFILE = {**PROFILE_BASE, **PROFILE_LOCALIZED["en"]}


def normalize_lang(lang: str | None) -> str:
    if not lang:
        return "en"
    normalized = lang.strip().lower()
    if normalized in SUPPORTED_LANGS:
        return normalized

    # Accept common locale formats like "tr-TR", "en_US", etc.
    base = normalized.split("-", 1)[0].split("_", 1)[0]
    if base in SUPPORTED_LANGS:
        return base

    return "en"


def get_lang(request: HttpRequest) -> str:
    # Prefer explicit query param.
    if "lang" in request.GET:
        return normalize_lang(request.GET.get("lang"))

    # Fall back to cookie when navigating via links that might drop the query.
    if "lang" in request.COOKIES:
        return normalize_lang(request.COOKIES.get("lang"))

    return "en"


def get_profile(lang: str) -> dict:
    safe_lang = normalize_lang(lang)
    profile = {**PROFILE_BASE, **PROFILE_LOCALIZED[safe_lang]}
    db_profile = PortfolioProfile.objects.first()
    if not db_profile:
        return profile

    def parse_lines(value: str, fallback: list[str]) -> list[str]:
        items = [line.strip() for line in value.splitlines() if line.strip()]
        return items or fallback

    return {
        **profile,
        "name": db_profile.name or profile["name"],
        "phone": db_profile.phone or profile["phone"],
        "email": db_profile.email or profile["email"],
        "github": db_profile.github or profile["github"],
        "linkedin": db_profile.linkedin or profile["linkedin"],
        "headline": getattr(db_profile, f"headline_{safe_lang}") or profile["headline"],
        "bio": getattr(db_profile, f"bio_{safe_lang}") or profile["bio"],
        "location": getattr(db_profile, f"location_{safe_lang}") or profile["location"],
        "roles": parse_lines(getattr(db_profile, f"roles_{safe_lang}") or "", profile["roles"]),
        "skills": parse_lines(getattr(db_profile, f"skills_{safe_lang}") or "", profile["skills"]),
        "languages": parse_lines(getattr(db_profile, f"languages_{safe_lang}") or "", profile["languages"]),
    }


def localized_text(project: Project, lang: str) -> tuple[str, str]:
    safe_lang = normalize_lang(lang)
    if safe_lang == "tr":
        return project.title_tr or project.title, project.description_tr or project.description
    if safe_lang == "ar":
        return project.title_ar or project.title, project.description_ar or project.description
    return project.title, project.description


def project_cards(projects, lang: str) -> list[dict]:
    safe_lang = normalize_lang(lang)
    labels = CATEGORY_LABELS[safe_lang]
    cards = []
    for project in projects:
        title, description = localized_text(project, safe_lang)
        cards.append(
            {
                "title": title,
                "description": description,
                "category": project.category,
                "category_label": labels.get(project.category, project.category),
                "tech_stack": project.tech_stack,
                "github_url": project.github_url,
                "live_url": project.live_url,
            }
        )
    return cards


def build_context(request: HttpRequest) -> dict:
    lang = get_lang(request)
    profile = get_profile(lang)
    return {
        "profile": profile,
        "lang": lang,
        "t": TRANSLATIONS[lang],
        "dir": "rtl" if lang == "ar" else "ltr",
        "lang_query": f"?lang={lang}",
        "canonical_url": request.build_absolute_uri(request.path),
    }


def home(request: HttpRequest) -> HttpResponse:
    lang = get_lang(request)
    featured_projects = Project.objects.filter(featured=True)[:6]
    context = {**build_context(request), "projects": project_cards(featured_projects, lang)}
    response = render(request, "portfolio/home.html", context)
    response.set_cookie("lang", lang, max_age=60 * 60 * 24 * 365, samesite="Lax")
    return response


def about(request: HttpRequest) -> HttpResponse:
    lang = get_lang(request)
    response = render(request, "portfolio/about.html", build_context(request))
    response.set_cookie("lang", lang, max_age=60 * 60 * 24 * 365, samesite="Lax")
    return response


def projects(request: HttpRequest) -> HttpResponse:
    lang = get_lang(request)
    all_projects = Project.objects.all()
    response = render(
        request,
        "portfolio/projects.html",
        {**build_context(request), "projects": project_cards(all_projects, lang)},
    )
    response.set_cookie("lang", lang, max_age=60 * 60 * 24 * 365, samesite="Lax")
    return response


def contact(request: HttpRequest) -> HttpResponse:
    lang = get_lang(request)
    response = render(request, "portfolio/contact.html", build_context(request))
    response.set_cookie("lang", lang, max_age=60 * 60 * 24 * 365, samesite="Lax")
    return response
