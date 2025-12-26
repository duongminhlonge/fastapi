FastAPI Project

This guide will help you **set up a virtual environment**, install dependencies, and run your FastAPI app using Uvicorn.

---

## 1. Prepare the environment

### 1.1. Create a virtual environment (if not already created)
```bash
# Create a virtual environment named "venv"
python -m venv venv
```

### 1.2. Activate the virtual environment
```bash
source venv/bin/activate
```

## 2. Install dependencies
```bash
pip install fastapi uvicorn
```
- If you have a requirements.txt file:
```bash
pip install -r requirements.txt
```

- After installing all required packages (e.g., FastAPI, Uvicorn, Black), save them to `requirements.txt` so others can install the same dependencies:
```bash
pip freeze > requirements.txt
```

## 3. Sample Project Structure
```bash
fastapi_project/
├├─ venv/                  # Virtual environment containing Python packages
├─ app/                   # Main application source code
│  ├─ __init__.py
│  ├─ main.py             # FastAPI app initialization, include routers, scheduler
│  ├─ core/               # Config, constants, settings (.env)
│  │  ├─ __init__.py
│  │  └─ config.py
│  ├─ api/                # Routers / endpoints, versioned
│  │  ├─ __init__.py
│  │  └─ v1/
│  │     ├─ __init__.py
│  │     └─ routes.py     # API endpoints version 1
│  ├─ models/             # SQLAlchemy or Pydantic models
│  │  ├─ __init__.py
│  │  └─ user.py
│  ├─ schemas/            # Pydantic schemas for request/response validation
│  │  ├─ __init__.py
│  │  └─ user.py
│  ├─ services/           # Business logic / use cases
│  │  ├─ __init__.py
│  │  └─ user_service.py
│  ├─ utils/              # Reusable helper functions
│  │  ├─ __init__.py
│  │  └─ email_utils.py
│  ├─ jobs/               # Cronjobs or scheduled tasks
│  │  ├─ __init__.py
│  │  └─ email_job.py
│  ├─ db/                 # Database connection, session, migration helpers
│  │  ├─ __init__.py
│  │  └─ base.py
│  └─ dependencies/       # Dependencies for FastAPI Depends()
│     ├─ __init__.py
│     └─ auth.py          # Example: get_current_user, verify_token, etc.
├─ alembic/               # Alembic migration scripts (parallel to app/)
│  ├─ versions/           # Individual migration files
│  ├─ env.py              # Alembic environment configuration
│  └─ script.py.mako      # Alembic template
├─ alembic.ini            # Alembic main configuration
├─ scripts/               # CLI scripts or cronjob scripts
│  └─ run_email_cron.py
├─ tests/                 # Unit/integration tests
│  ├─ __init__.py
│  └─ test_email.py
├─ requirements.txt       # Project dependencies
└─ README.md
```
## 4. Run the FastAPI App
- Navigate to the project root directory (fastapi_project/):
```bash
cd /path/to/fastapi_project
```
- Run Uvicorn:
```bash
uvicorn app.main:app --reload
```
- Open in browser:
```bash
http://127.0.0.1:8000
```
- Swagger API docs:
```bash
http://127.0.0.1:8000/docs
```

## 5. Install Black and Flake8 (Format code PEP8)
```bash
# Install Black for auto-formatting
pip install black

# Install Flake8 for linting
pip install flake8
```

- Format code with Black
```bash
black .
```

- Check code style with Flake8
```bash
flake8 app/
```