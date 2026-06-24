# Task Manager

A Django REST API for managing projects, tasks, comments, and users.

## Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* Docker
* GitLab CI/CD
* Nginx
* Gunicorn

## Project Structure

```
task-manager/
├── backend/
├── docs/
├── scripts/
├── README.md
└── .gitignore
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the server:

```bash
python manage.py runserver
```
