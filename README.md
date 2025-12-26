# FastAPI Project (Docker Setup)

This guide helps you **set up and run your FastAPI project using Docker**, PostgreSQL, and Nginx with a virtual host
`fastapi.local`.

---

## 1. Prerequisites

- Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/).
- Make sure your system can resolve `fastapi.local`. Add this to `/etc/hosts` (Linux/macOS) or
  `C:\Windows\System32\drivers\etc\hosts` (Windows):

```bash
127.0.0.1 fastapi.local
```

- Ensure ports **80**, **443**, and **8000** are available.

---

## 2. Environment Variables

- Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

- Example `.env` contents:

```bash
DATABASE_URL=postgresql+psycopg2://user:password@db:5432/fastapi
SECRET_KEY=your_super_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

- Docker Compose will read this file automatically.

---

## 3. Docker Project Structure

```bash
fastapi_project/
├─ app/                   # FastAPI source code
│  ├─ main.py             # FastAPI app init, routers, etc.
│  ├─ core/               # Config and constants
│  ├─ api/                # Versioned API routers
│  ├─ models/             # SQLAlchemy ORM models
│  ├─ schemas/            # Pydantic schemas
│  ├─ services/           # Business logic
│  ├─ utils/              # Helper functions
│  ├─ jobs/               # Scheduled tasks / cronjobs
│  ├─ db/                 # Database connection & Base
│  └─ dependencies/       # FastAPI Depends() utilities
├─ alembic/               # Database migration scripts
├─ nginx/                 # Nginx config files
│  └─ nginx.conf
├─ docker-compose.yml     # Docker Compose setup
├─ Dockerfile             # Docker image for FastAPI
├─ .env.example           # Template for environment variables
├─ scripts/               # CLI scripts / cronjob scripts
├─ tests/                 # Unit/integration tests
└─ README.md

```

---

## 4. Build and Start the Project with Docker

1. Build the Docker images:

```bash
docker-compose build
```

2. Start all services (FastAPI, PostgreSQL, Nginx):

```bash
docker-compose up -d
```

- This will start 3 containers:
    - fastapi_db → PostgreSQL
    - fastapi_app → FastAPI
    - fastapi_nginx → Nginx serving virtual host `fastapi.local`

3. Check running containers:

```bash
docker ps
```

---

## 5. Database Migrations

- Run Alembic migrations:

```bash
docker-compose exec app alembic upgrade head
```

---

## 6. Access the Application

- Open in browser:

```bash
http://fastapi.local
```

- Swagger API docs:

```bash
http://fastapi.local/docs
```

- FastAPI automatically reloads code changes inside Docker if you mount volumes (see `docker-compose.yml`).

---

## 7. Logs and Debugging

- View container logs:

```bash
docker-compose logs -f app
docker-compose logs -f nginx
docker-compose logs -f db
```

- Enter FastAPI container shell:

```bash
docker-compose exec app /bin/sh
```

- Check Docker network:

```bash
docker network ls
docker network inspect fastapi_project_default
```

---

## 8. Stop the Project

```bash
docker-compose down
```

- Remove containers but keep database volume:

```bash
docker-compose down -v  # WARNING: deletes database data
```

---

## 9. Formatting and Linting (Optional, for dev)

- Install Black and Flake8 inside your local Python environment (not needed in Docker):

```bash
pip install black flake8
```

- Format code:

```bash
black app/
```

- Lint code:

```bash
flake8 app/
```

---

## 10. Run Unit Tests in Docker

Run tests in the app container:

```bash
docker exec -it fastapi_app bash
# now you are inside the container
pytest tests/ --disable-warnings -v
```

---

## 11. Python Dependencies and requirements.txt

If you want to run FastAPI locally (not strictly needed in Docker), install the required packages:

```bash
pip install fastapi uvicorn[standard] sqlalchemy psycopg2-binary pydantic python-dotenv alembic python-jose[cryptography] passlib[bcrypt]
```

- fastapi → main framework

- uvicorn[standard] → ASGI server for running FastAPI

- sqlalchemy → ORM for database models

- psycopg2-binary → PostgreSQL driver

- pydantic → data validation / schemas

- python-dotenv → load .env files

- alembic → database migrations

- python-jose[cryptography] → JWT token creation / verification

- passlib[bcrypt] → password hashing

After installing all packages, freeze them into requirements.txt:

```bash
pip freeze > requirements.txt
```

Anyone can now install the exact versions:

```bash
pip install -r requirements.txt

```

---
✅ This setup ensures your FastAPI project runs **fully in Docker**, with PostgreSQL, Nginx virtual host (
`fastapi.local`), and automatic environment configuration.
