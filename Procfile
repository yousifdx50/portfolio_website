web: python manage.py migrate && python manage.py seed_profile && gunicorn portfolio_site.asgi:application -k uvicorn.workers.UvicornWorker
