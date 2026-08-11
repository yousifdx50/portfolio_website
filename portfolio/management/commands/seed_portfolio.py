from django.core.management.base import BaseCommand

from portfolio.models import Project


SEED_PROJECTS = [
    {
        "titles": {
            "en": "Automation Process Workflow System",
            "tr": "Otomasyon S\u00fcre\u00e7 Is Ak\u0131\u015f\u0131 Sistemi",
            "ar": "\u0646\u0638\u0627\u0645 \u0623\u062a\u0645\u062a\u0629 \u0633\u064a\u0631 \u0627\u0644\u0639\u0645\u0644",
        },
        "descriptions": {
            "en": (
                "Designed backend architecture and REST APIs to model complex automation process workflows "
                "with reliable state transitions."
            ),
            "tr": (
                "Karma\u015f\u0131k otomasyon s\u00fcre\u00e7leri i\u00e7in backend mimarisi ve g\u00fcvenilir durum ge\u00e7i\u015fleri "
                "sa\u011flayan REST API yap\u0131s\u0131 geli\u015ftirildi."
            ),
            "ar": (
                "\u062a\u0645 \u062a\u0635\u0645\u064a\u0645 \u0645\u0639\u0645\u0627\u0631\u064a\u0629 Backend \u0648\u0628\u0646\u0627\u0621 REST APIs "
                "\u0644\u0646\u0645\u0630\u062c\u0629 \u0639\u0645\u0644\u064a\u0627\u062a \u0627\u0644\u0623\u062a\u0645\u062a\u0629 \u0627\u0644\u0645\u0639\u0642\u062f\u0629 "
                "\u0645\u0639 \u0627\u0646\u062a\u0642\u0627\u0644\u0627\u062a \u062d\u0627\u0644\u0629 \u0645\u0648\u062b\u0648\u0642\u0629."
            ),
        },
        "category": "backend_dev",
        "tech_stack": "Python, FastAPI, PostgreSQL",
    },
    {
        "titles": {
            "en": "E-Commerce Backend API",
            "tr": "E-Ticaret Backend API",
            "ar": "\u0648\u0627\u062c\u0647\u0629 Backend \u0644\u0645\u062a\u062c\u0631 \u0625\u0644\u0643\u062a\u0631\u0648\u0646\u064a",
        },
        "descriptions": {
            "en": (
                "Built an online-store backend with authentication, inventory management, and secure CRUD "
                "operations for products and orders."
            ),
            "tr": (
                "Kullan\u0131c\u0131 giri\u015fi, envanter y\u00f6netimi ve \u00fcr\u00fcn-sipari\u015f CRUD i\u015flemleri i\u00e7in "
                "g\u00fcvenli bir online ma\u011faza backend API'si geli\u015ftirildi."
            ),
            "ar": (
                "\u0628\u0646\u0627\u0621 API \u062e\u0644\u0641\u064a \u0644\u0645\u062a\u062c\u0631 \u0625\u0644\u0643\u062a\u0631\u0648\u0646\u064a "
                "\u064a\u0634\u0645\u0644 \u0627\u0644\u0645\u0635\u0627\u062f\u0642\u0629 \u0648\u0625\u062f\u0627\u0631\u0629 \u0627\u0644\u0645\u062e\u0632\u0648\u0646 "
                "\u0648\u0639\u0645\u0644\u064a\u0627\u062a CRUD \u0627\u0644\u0622\u0645\u0646\u0629."
            ),
        },
        "category": "web_dev",
        "tech_stack": "Java, Spring Boot, PostgreSQL",
    },
    {
        "titles": {
            "en": "ML and Automation Developer Project",
            "tr": "ML ve Otomasyon Gelistirici Projesi",
            "ar": "\u0645\u0634\u0631\u0648\u0639 \u0645\u0637\u0648\u0631 \u062a\u0639\u0644\u0645 \u0627\u0644\u0622\u0644\u0629 \u0648\u0627\u0644\u0623\u062a\u0645\u062a\u0629",
        },
        "legacy_titles": [
            "ML Portfolio Starter",
            "ML Portf\u00f6y Ba\u015flang\u0131\u00e7 Projesi",
            "\u0628\u062f\u0627\u064a\u0629 \u0645\u0634\u0631\u0648\u0639 ML \u0644\u0644\u0628\u0648\u0631\u062a\u0641\u0648\u0644\u064a\u0648",
        ],
        "descriptions": {
            "en": (
                "An ML and automation development project focused on model pipelines, automated workflows, "
                "and data visualization for practical production use."
            ),
            "tr": (
                "Model hatlari, otomatik is akislari ve veri gorsellestirme uzerine odaklanan; "
                "uretim odakli bir ML ve otomasyon gelistirme projesi."
            ),
            "ar": (
                "\u0645\u0634\u0631\u0648\u0639 \u062a\u0637\u0648\u064a\u0631 \u064a\u0631\u0643\u0632 \u0639\u0644\u0649 \u062a\u0639\u0644\u0645 \u0627\u0644\u0622\u0644\u0629 "
                "\u0648\u0627\u0644\u0623\u062a\u0645\u062a\u0629\u060c \u0648\u064a\u0634\u0645\u0644 \u062e\u0637\u0648\u0637 \u0646\u0645\u0627\u0630\u062c\u060c "
                "\u062a\u062f\u0641\u0642\u0627\u062a \u0639\u0645\u0644 \u0622\u0644\u064a\u0629\u060c \u0648\u062a\u0635\u0648\u064a\u0631 \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a."
            ),
        },
        "category": "ml_dev",
        "tech_stack": "PyTorch, NumPy, Pandas, Matplotlib",
    },
]


def pick_text(values: dict[str, str], lang: str) -> str:
    return values.get(lang) or values["en"]


class Command(BaseCommand):
    help = "Seeds starter portfolio projects"

    def add_arguments(self, parser):
        parser.add_argument(
            "--lang",
            default="en",
            choices=["en", "tr", "ar"],
            help="Language for seeded project text (default: en).",
        )

    def handle(self, *args, **options):
        lang = options["lang"]
        created = 0

        for item in SEED_PROJECTS:
            defaults = {
                "title": pick_text(item["titles"], lang),
                "title_tr": item["titles"]["tr"],
                "title_ar": item["titles"]["ar"],
                "description": pick_text(item["descriptions"], lang),
                "description_tr": item["descriptions"]["tr"],
                "description_ar": item["descriptions"]["ar"],
                "category": item["category"],
                "tech_stack": item["tech_stack"],
            }
            existing = Project.objects.filter(
                category=item["category"],
                title__in=[
                    item["titles"]["en"],
                    item["titles"]["tr"],
                    item["titles"]["ar"],
                    *item.get("legacy_titles", []),
                ],
            ).first()

            if existing:
                for field, value in defaults.items():
                    setattr(existing, field, value)
                existing.save()
                continue

            Project.objects.create(**defaults)
            created += 1

        self.stdout.write(self.style.SUCCESS(f"Seed complete for '{lang}'. Added {created} project(s)."))
