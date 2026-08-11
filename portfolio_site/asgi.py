import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_site.settings")
from django.conf import settings  # noqa: E402
from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler  # type: ignore  # noqa: E402
from django.core.asgi import get_asgi_application  # noqa: E402
from django.db import close_old_connections  # noqa: E402
from fastapi import FastAPI  # noqa: E402

django_asgi_app = get_asgi_application()
if settings.DEBUG:
    django_asgi_app = ASGIStaticFilesHandler(django_asgi_app)

from portfolio.api import router as portfolio_router  # noqa: E402

fastapi_app = FastAPI(title="Portfolio API", version="1.0.0", root_path="/api")
fastapi_app.include_router(portfolio_router)

@fastapi_app.middleware("http")
async def django_db_connection_middleware(request, call_next):
    close_old_connections()
    response = await call_next(request)
    close_old_connections()
    return response


async def application(scope, receive, send):
    path = scope.get("path", "")
    if path.startswith("/api"):
        await fastapi_app(scope, receive, send)
    else:
        await django_asgi_app(scope, receive, send)
