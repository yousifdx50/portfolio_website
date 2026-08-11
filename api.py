from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from asgiref.sync import sync_to_async
from portfolio.models import Project

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

@router.get("/projects", response_model=List[ProjectOut])
async def get_projects():
    projects = await sync_to_async(list)(Project.objects.all().values())
    return projects