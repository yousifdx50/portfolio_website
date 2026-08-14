import pytest
from httpx import ASGITransport, AsyncClient
from asgiref.sync import sync_to_async
from portfolio.models import Project, PortfolioProfile
from portfolio_site.asgi import fastapi_app # Import your FastAPI app


@pytest.mark.asyncio
async def test_health_check():
    transport = ASGITransport(app=fastapi_app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_get_projects_api():
    # Create some test data using sync_to_async because ORM is sync
    await sync_to_async(Project.objects.create)(
        title="API Project 1",
        description="Description 1",
        category="web_dev",
        tech_stack="FastAPI",
        featured=True,
    )
    await sync_to_async(Project.objects.create)(
        title="API Project 2",
        description="Description 2",
        category="backend_dev",
        tech_stack="Django",
        featured=False,
    )

    transport = ASGITransport(app=fastapi_app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # The API sorts by -created_at, so the newest project ("API Project 2") will be first.
        response = await ac.get("/api/projects")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["title"] == "API Project 2"
    assert data[1]["title"] == "API Project 1"
