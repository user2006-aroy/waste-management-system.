# Waste Management System — Django + SQLite

A working full-stack starter website inspired by the supplied dashboard reference.

## Features
- Responsive citizen-facing dashboard inspired by the screenshot
- Complaint submission form with optional image upload
- Unique ticket ID generated for every complaint
- Complaint tracking using ticket ID + email
- Citizen registration, login and logout
- Live dashboard counts (total, pending, in progress, resolved)
- Public category report page
- Waste awareness page
- Django admin for municipal staff to review complaints, update status and add admin notes
- SQLite database included through Django's built-in SQLite backend

## Requirements
- Python 3.10+
- pip

## Run locally (Windows PowerShell)
```powershell
cd waste_management_system
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```
Open http://127.0.0.1:8000

## Run locally (macOS / Linux)
```bash
cd waste_management_system
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
- Citizen website: http://127.0.0.1:8000
- Admin dashboard: http://127.0.0.1:8000/admin/

## Admin workflow
1. Sign in at `/admin/` using the superuser created above.
2. Open **Complaints**.
3. Search/filter by ticket, category, status or date.
4. Change the status to Pending / In Progress / Resolved.
5. Add an admin note. The citizen can see it when tracking with ticket ID + email.

## Database
Django creates `db.sqlite3` automatically in the project root after `python manage.py migrate`. No separate database server is required.

## Important before deployment
This is a local-development starter. Before production, set `DEBUG = False`, use a strong environment-based `SECRET_KEY`, configure `ALLOWED_HOSTS`, serve static/media files securely, enable HTTPS, and review privacy/retention rules for uploaded citizen data. Do not use the sample secret key in production.
