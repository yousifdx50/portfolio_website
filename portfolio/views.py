from functools import wraps
from django.http import HttpRequest, HttpResponse
from django.core.cache import cache
from django.shortcuts import render

from .models import PortfolioProfile, Project

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
        "backend_identity": "Backend Software Engineer",
        "hero_statement": "I build reliable backend systems, APIs, and automation products.",
        "hero_stack": "Java • Spring Boot • Python • PostgreSQL • REST APIs • AI/ML",
        "view_projects": "View Projects",
        "contact_me": "Contact Me",
        "connect": "Connect",
        "view_project": "View Project",
        "live_demo": "Live Demo",
        "what_i_build": "What I Build",
        "backend_systems": "Backend Systems",
        "rest_apis": "REST APIs",
        "ai_machine_learning": "AI & Machine Learning",
        "automation_systems": "Automation Systems",
        "tech_stack_section": "Tech Stack",
        "backend": "Backend",
        "database": "Database",
        "ai_data": "AI / Data",
        "tools": "Tools",
        "services": "Services / What I Can Build",
        "final_cta_title": "Have a project in mind?",
        "final_cta_text": "Let's build it.",
        "work_together": "Let's Work Together",
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
        "backend_identity": "Backend Yazilim Muhendisi",
        "hero_statement": "Guvenilir backend sistemleri, API'ler ve otomasyon urunleri gelistiriyorum.",
        "hero_stack": "Java • Spring Boot • Python • PostgreSQL • REST API'leri • AI/ML",
        "view_projects": "Projeleri Gor",
        "contact_me": "Iletisime Gec",
        "connect": "Baglan",
        "view_project": "Projeyi Gor",
        "live_demo": "Canli Demo",
        "what_i_build": "Ne Insaa Ediyorum",
        "backend_systems": "Backend Sistemleri",
        "rest_apis": "REST API'leri",
        "ai_machine_learning": "Yapay Zeka ve Makine Ogrenmesi",
        "automation_systems": "Otomasyon Sistemleri",
        "tech_stack_section": "Teknoloji Yigini",
        "backend": "Backend",
        "database": "Veritabani",
        "ai_data": "AI / Veri",
        "tools": "Araclar",
        "services": "Hizmetler / Neler Gelistirebilirim",
        "final_cta_title": "Aklinda bir proje mi var?",
        "final_cta_text": "Birlikte gelistirelim.",
        "work_together": "Birlikte Calisalim",
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
        "backend_identity": "مهندس برمجيات Backend",
        "hero_statement": "أبني أنظمة Backend وواجهات API ومنتجات أتمتة موثوقة.",
        "hero_stack": "Java • Spring Boot • Python • PostgreSQL • REST APIs • AI/ML",
        "view_projects": "عرض المشاريع",
        "contact_me": "تواصل معي",
        "connect": "تواصل",
        "view_project": "عرض المشروع",
        "live_demo": "نسخة مباشرة",
        "what_i_build": "ما أبنيه",
        "backend_systems": "أنظمة Backend",
        "rest_apis": "واجهات REST API",
        "ai_machine_learning": "الذكاء الاصطناعي وتعلم الآلة",
        "automation_systems": "أنظمة الأتمتة",
        "tech_stack_section": "المجموعة التقنية",
        "backend": "Backend",
        "database": "قاعدة البيانات",
        "ai_data": "الذكاء الاصطناعي / البيانات",
        "tools": "الأدوات",
        "services": "الخدمات / ما يمكنني بناؤه",
        "final_cta_title": "هل لديك مشروع في ذهنك؟",
        "final_cta_text": "لنبنه معاً.",
        "work_together": "لنعمل معاً",
    },
}

SUPPORTED_LANGS = ("en", "tr", "ar")


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
    """
    Fetches the singleton PortfolioProfile from the database and formats it for the template.
    Returns a dictionary with profile data, or an empty dictionary if not found.
    """
    cache_key = f"profile_data_{lang}"
    cached_profile = cache.get(cache_key)
    if cached_profile:
        return cached_profile

    db_profile = PortfolioProfile.objects.first()  # This hits the DB
    if not db_profile:
        return {}

    def parse_lines(value: str) -> list[str]:
        items = [line.strip() for line in value.splitlines() if line.strip()]
        return items

    profile_data = {
        "name": db_profile.name,
        "phone": db_profile.phone,
        "email": db_profile.email,
        "github": db_profile.github,
        "linkedin": db_profile.linkedin,
        "headline": getattr(db_profile, f"headline_{lang}"),
        "bio": getattr(db_profile, f"bio_{lang}"),
        "location": getattr(db_profile, f"location_{lang}"),
        "roles": parse_lines(getattr(db_profile, f"roles_{lang}")),
        "skills": parse_lines(getattr(db_profile, f"skills_{lang}")),
        "languages": parse_lines(getattr(db_profile, f"languages_{lang}")),
    }
    # Cache the result for 5 minutes
    cache.set(cache_key, profile_data, timeout=300)
    return profile_data


def set_language_cookie(view_func):
    """A decorator that sets the language cookie on the response."""

    @wraps(view_func)
    def _wrapped_view(request: HttpRequest, *args, **kwargs) -> HttpResponse:
        response = view_func(request, *args, **kwargs)
        response.set_cookie("lang", get_lang(request), max_age=60 * 60 * 24 * 365, samesite="Lax")
        return response

    return _wrapped_view


def localized_text(project: Project, lang: str) -> tuple[str, str]:
    # Assumes lang is already normalized
    if lang == "tr":
        return project.title_tr or project.title, project.description_tr or project.description
    if lang == "ar":
        return project.title_ar or project.title, project.description_ar or project.description
    return project.title, project.description


def localized_project_details(project: Project, lang: str) -> tuple[str, list[str]]:
    if lang == "tr":
        problem_statement = project.problem_statement_tr or project.problem_statement
        features = project.features_tr or project.features
    elif lang == "ar":
        problem_statement = project.problem_statement_ar or project.problem_statement
        features = project.features_ar or project.features
    else:
        problem_statement = project.problem_statement
        features = project.features

    return problem_statement, [line.strip() for line in features.splitlines() if line.strip()]


def project_cards(projects, lang: str) -> list[dict]:
    cards = []
    for project in projects:
        title, description = localized_text(project, lang)
        problem_statement, features = localized_project_details(project, lang)
        technologies = [item.strip() for item in project.tech_stack.split(",") if item.strip()]
        cards.append(
            {
                "title": title,
                "description": description,
                "problem_statement": problem_statement,
                "features": features,
                "technologies": technologies,
                "category": project.category,
                "category_label": project.get_category_display(),
                "tech_stack": project.tech_stack,
                "project_image": project.project_image,
                "architecture_image": project.architecture_image,
                "github_url": project.github_url,
                "live_url": project.live_url,
                "primary_url": project.live_url or project.github_url,
                "featured": project.featured,
            }
        )
    return cards


def build_context(request: HttpRequest) -> dict:
    lang = get_lang(request)
    profile = get_profile(lang)
    translations = TRANSLATIONS.get(lang, TRANSLATIONS["en"])
    return {
        "profile": profile,
        "lang": lang,
        "t": translations,
        "capabilities": [
            {"title": translations["backend_systems"], "description": "Scalable services and maintainable business logic."},
            {"title": translations["rest_apis"], "description": "Secure, documented APIs that connect products and data."},
            {"title": translations["ai_machine_learning"], "description": "Practical data and model workflows for production use."},
            {"title": translations["automation_systems"], "description": "Reliable workflows that reduce repetitive operational work."},
        ],
        "tech_stack_groups": [
            {"title": translations["backend"], "items": ["Java", "Spring Boot", "Python", "FastAPI"]},
            {"title": translations["database"], "items": ["PostgreSQL", "MySQL"]},
            {"title": translations["ai_data"], "items": ["PyTorch", "Pandas", "NumPy"]},
            {"title": translations["tools"], "items": ["Git", "Docker", "REST APIs"]},
        ],
        "services": [
            "Custom REST APIs",
            "Backend applications",
            "Database systems",
            "Automation software",
            "AI/ML applications",
            "E-commerce backends",
        ],
        "dir": "rtl" if lang == "ar" else "ltr",
        "lang_query": f"?lang={lang}",
        "canonical_url": request.build_absolute_uri(request.path),
    }


@set_language_cookie
def home(request: HttpRequest) -> HttpResponse:
    context = build_context(request)
    featured_projects = []
    if context.get("profile"):
        featured_projects = Project.objects.filter(featured=True)[:6]
    context["projects"] = project_cards(featured_projects, context["lang"])
    return render(request, "portfolio/home.html", context)


@set_language_cookie
def about(request: HttpRequest) -> HttpResponse:
    return render(request, "portfolio/about.html", build_context(request))


@set_language_cookie
def projects(request: HttpRequest) -> HttpResponse:
    context = build_context(request)
    all_projects = Project.objects.all()
    context["projects"] = project_cards(all_projects, context["lang"])
    return render(request, "portfolio/projects.html", context)


@set_language_cookie
def contact(request: HttpRequest) -> HttpResponse:
    return render(request, "portfolio/contact.html", build_context(request))
