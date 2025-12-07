# Mini HR Leave Management

Mini HR Leave Management is a lightweight Django application for managing employee leave requests with an approval workflow for administrators. It is intended as a small, easy-to-deploy project suitable for learning, prototyping, or small teams.

## Features
- **User authentication:** Signup, login, logout, password reset flows.
- **Leave requests:** Employees can apply for leave and view request history.
- **Admin approval:** Admin dashboard to review, approve, or reject leave requests.
- **Clean templates & static assets:** Simple HTML templates and CSS for quick UI.
- **Migrations included:** Database schema managed via Django migrations.

## Quick Start
- **Clone repository:** (if not already cloned)
  - `git clone https://github.com/hassansaif1/Mini_HR-Management-System.git`
- **Create virtual environment:** (PowerShell)
  - `python -m venv .venv`
  - `.venv\Scripts\Activate.ps1`
- **Install dependencies:**
  - `pip install -r requirements.txt`
- **Configure settings:**
  - Edit `minihrmanagement/settings.py` to set `SECRET_KEY`, `DEBUG`, and `DATABASES` (MySQL or SQLite).
- **Apply migrations:**
  - `python manage.py migrate`
- **Create a superuser:**
  - `python manage.py createsuperuser`
- **Run development server:**
  - `python manage.py runserver`

## Project Structure (high-level)
- **Project:** `minihrmanagement/`
  - `settings.py`, `urls.py`, `wsgi.py`, `asgi.py`
- **Core app:** `core/`
  - `models.py` — contains `LeaveRequest` model
  - `forms.py` — leave application form
  - `views.py` — user and admin views
  - `admin.py` — admin registration
  - `migrations/` — migration files
- **Templates:** `templates/` — UI pages (login, signup, leave forms, admin)
- **Static assets:** `static/` — CSS and other static files
- **Entrypoint:** `manage.py`

## Configuration Notes
- **Static files:** Ensure `STATICFILES_DIRS` in `minihrmanagement/settings.py` points to `static/` for development.
- **Email:** If you use password reset, configure SMTP credentials in `settings.py`.
- **Database:** Default may be MySQL in the supplied settings. For quick setup, switch to SQLite by updating `DATABASES` in `settings.py`:
  - Example SQLite:
    ```python
    DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
      }
    }
    ```

## Testing
- **Run Django tests:**
  - `python manage.py test`
- Add tests under `core/tests.py` for coverage of business logic and views.

## Deployment (brief)
- Set `DEBUG = False`, configure `ALLOWED_HOSTS`, and set a secure `SECRET_KEY`.
- Use a production-ready server (e.g., Gunicorn + Nginx) and configure static file serving.
- Run `python manage.py collectstatic` when deploying.

## Contributing
- **Issues & PRs:** Please open an issue before a larger change; small fixes can go directly as PRs.
- **Coding style:** Maintain current project style; add tests for new features.
- **Local checks:** Run `python manage.py test` and verify the dev server runs locally.

## License
- Add a license file or clause here (e.g., MIT, Apache-2.0). Replace this placeholder as desired.

## Maintainer / Contact
- **Repository owner:** `hassansaif1` (GitHub)
- For questions or collaboration, open an issue or contact via your GitHub profile.

---
