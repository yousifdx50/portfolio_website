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
        slug="api-project-1",
        title="API Project 1",
        description="Description 1",
        title_tr="API Proje 1",
        description_tr="Açıklama 1",
        category="web_dev",
        tech_stack="FastAPI",
        featured=True,
    )
    await sync_to_async(Project.objects.create)(
        slug="api-project-2",
        title="API Project 2",
        description="Description 2",
        category="backend_dev",
        tech_stack="Django",
        featured=False,
    )

    transport = ASGITransport(app=fastapi_app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # The API sorts by -created_at, so the newest project ("API Project 2") will be first.
        # Test default language (en)
        response_en = await ac.get("/api/projects")
        # Test Turkish language
        response_tr = await ac.get("/api/projects?lang=tr")

    # Assert English response
    assert response_en.status_code == 200
    data_en = response_en.json()
    assert len(data_en) == 2
    assert data_en[0]["title"] == "API Project 2"  # Default English title
    assert data_en[1]["title"] == "API Project 1"

    # Assert Turkish response
    assert response_tr.status_code == 200
    data_tr = response_tr.json()
    assert len(data_tr) == 2
    assert data_tr[1]["title"] == "API Proje 1"  # Turkish title


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_get_profile_api():
    # Create a test profile with localized data
    await sync_to_async(PortfolioProfile.objects.create)(
        name="Test User",
        headline_en="English Headline",
        headline_tr="Turkish Headline",
        bio_en="English bio.",
        bio_tr="Turkish bio.",
    )

    transport = ASGITransport(app=fastapi_app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Test default language (en)
        response_en = await ac.get("/api/profile")
        # Test Turkish language
        response_tr = await ac.get("/api/profile?lang=tr")

    # Assert English response
    assert response_en.status_code == 200
    assert response_en.json()["headline"] == "English Headline"

    # Assert Turkish response
    assert response_tr.status_code == 200
    assert response_tr.json()["headline"] == "Turkish Headline"
