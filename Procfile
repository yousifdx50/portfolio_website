web: python manage.py migrate && python manage.py collectstatic --noinput && python manage.py seed_profile && gunicorn portfolio_site.wsgi:application --bind 0.0.0.0:$PORT
