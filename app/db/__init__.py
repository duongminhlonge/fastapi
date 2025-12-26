# app/db/__init__.py

# This file makes 'db' a Python package.
# You can optionally import Base, engine, SessionLocal here
# so that other modules can do:
# from app.db import Base, SessionLocal, get_db

from app.db.base import Base, engine, SessionLocal, get_db
