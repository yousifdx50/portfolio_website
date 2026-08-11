from fastapi import APIRouter
from pydantic import BaseModel
from asgiref.sync import sync_to_async

from .models import Project

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
async def get_projects():
    projects = await sync_to_async(list)(
        Project.objects.order_by("created_at").values(
            "title",
            "description",
            "category",
            "tech_stack",
            "github_url",
            "live_url",
            "featured",
        )
    )
    return projects
