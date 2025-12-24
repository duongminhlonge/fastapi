from sqlalchemy.orm import declarative_base

# All models will inherit from this Base
Base = declarative_base()

# Import all models here for Alembic autogenerate
from app.models.user import User

# If you add more models, import them here as well
# from app.models.product import Product
