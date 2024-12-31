import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/fastapi_forms")
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
