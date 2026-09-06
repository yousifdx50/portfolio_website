from fastapi import APIRouter, Query
from pydantic import BaseModel
from asgiref.sync import sync_to_async

from .models import PortfolioProfile, Project
from .views import normalize_lang, localized_text

router = APIRouter()


class ProjectOut(BaseModel):
    title: str
    description: str
    category: str
    tech_stack: str
    github_url: str | None = None
    live_url: str | None = None
    featured: bool


class ProfileOut(BaseModel):
    name: str
    phone: str
    email: str
    github: str
    linkedin: str
    headline: str
    bio: str
    location: str


@router.get("/health")
async def health_check():
    """
    A simple health check endpoint for the API.
    """
    return {"status": "ok"}


@router.get("/projects", response_model=list[ProjectOut])
async def get_projects(
    lang: str = "en",
    limit: int = Query(10, gt=0, le=100),
    offset: int = Query(0, ge=0),
):
    """
    Get a paginated list of projects, localized to the requested language.
    """
    safe_lang = normalize_lang(lang)

    @sync_to_async
    def _get_projects():
        projects_qs = Project.objects.order_by("-created_at", "-id")[offset : offset + limit]
        results = []
        for p in projects_qs:
            title, description = localized_text(p, safe_lang)
            # Directly construct ProjectOut from model instance and localized text
            project_out = ProjectOut(
                title=title,
                description=description,
                category=p.category,
                tech_stack=p.tech_stack,
                github_url=p.github_url,
                live_url=p.live_url,
                featured=p.featured,
            )
            results.append(project_out)
        return results

    return await _get_projects()


@router.get("/profile", response_model=ProfileOut)
async def get_profile(lang: str = "en"):
    safe_lang = normalize_lang(lang)

    @sync_to_async
    def _get_profile():
        profile = PortfolioProfile.objects.first()
        if profile is None:
            return ProfileOut(
                name="",
                phone="",
                email="",
                github="",
                linkedin="",
                headline="",
                bio="",
                location="",
            )
        return ProfileOut(
            name=profile.name,
            phone=profile.phone,
            email=profile.email,
            github=profile.github,
            linkedin=profile.linkedin,
            headline=getattr(profile, f"headline_{safe_lang}"),
            bio=getattr(profile, f"bio_{safe_lang}"),
            location=getattr(profile, f"location_{safe_lang}"),
        )

    return await _get_profile()
