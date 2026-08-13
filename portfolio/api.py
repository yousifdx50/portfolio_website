from fastapi import APIRouter, Query
from pydantic import BaseModel
from asgiref.sync import sync_to_async

from .models import Project
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
        projects_qs = Project.objects.order_by("-created_at")[offset : offset + limit]
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
