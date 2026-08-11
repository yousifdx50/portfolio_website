# Django + FastAPI Portfolio

A starter portfolio backend where:
- Django serves website pages and admin.
- FastAPI serves JSON APIs under `/api`.

## Quickstart

1. Create and activate a virtual environment:
   ```bash
   # Create the environment
   py -m venv .venv
   # Activate on Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   # Or on Windows (Command Prompt)
   .venv\Scripts\activate.bat
   # Or on macOS/Linux
   source .venv/bin/activate
   ```
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run migrations:
   `python manage.py migrate`
4. Seed sample projects:
   `python manage.py seed_portfolio`
   `python manage.py seed_portfolio --lang tr`
   `python manage.py seed_portfolio --lang ar`
   This now fills multilingual project fields (`title_tr`, `title_ar`, `description_tr`, `description_ar`).
5. Seed profile (optional):
   `python manage.py seed_profile`
   Then edit profile content from `/admin` -> `Portfolio Profile`.
5. Create admin user:
   `python manage.py createsuperuser`
6. Run app (ASGI with Django + FastAPI):
   `uvicorn portfolio_site.asgi:application --reload`

## Routes

- Website: `/`, `/about/`, `/projects/`, `/contact/`
- Admin: `/admin/`
- FastAPI: `/api/health`, `/api/profile`, `/api/projects`
  - Language-aware:
    - `/api/profile?lang=en|tr|ar`
    - `/api/projects?lang=en|tr|ar`

## Database Setup

This project supports both SQLite and PostgreSQL.

- Local default: SQLite (`DB_ENGINE=sqlite`)
- Production recommended: PostgreSQL via `DATABASE_URL`

### SQLite (default)

1. Keep `DB_ENGINE=sqlite` in your env.
2. Run:
   - `python manage.py migrate`

### PostgreSQL (recommended for production)

1. Set either:
   - `DATABASE_URL=postgresql://user:password@host:5432/dbname`
   or manual fields (`DB_ENGINE=postgresql`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`).
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Run:
   - `python manage.py migrate`

## Customize

- Replace placeholder identity in `portfolio/views.py`.
- Add real project entries in Django admin.

## Deployment UI Checklist

Before deploying, quickly verify:
- `EN/TR/AR` switch works on all main pages (`/`, `/about/`, `/projects/`, `/contact/`).
- RTL layout is clean in Arabic (`/?lang=ar`, `/about/?lang=ar`, `/contact/?lang=ar`).
- Mobile layout has no overflow (check around 360px width).
- Navbar active page highlight updates correctly.
- Empty project states render as styled info cards.
- Social preview and favicon load:
  - `{domain}/static/favicon.svg`
  - `{domain}/static/img/og-placeholder.svg`
- Open Graph tags are present in page source (`og:title`, `og:description`, `og:image`, `twitter:card`).

## Production Run Notes

1. Set env values:
   - `DEBUG=False`
   - `SECRET_KEY=<strong-random-value>`
   - `ALLOWED_HOSTS=<your-domain>,<your-platform-domain>`
   - `CSRF_TRUSTED_ORIGINS=https://<your-domain>,https://<your-platform-domain>`
2. Collect static files:
   - `python manage.py collectstatic --noinput`
3. Run migrations:
   - `python manage.py migrate`
4. Start server (example):
   - `uvicorn portfolio_site.asgi:application --host 0.0.0.0 --port 8000`
