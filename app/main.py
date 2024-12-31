from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.forms.routes import router as forms_router
from app.database import init_db

app = FastAPI()

# Initialize the database
@app.on_event("startup")
async def startup():
    await init_db()

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(forms_router, prefix="/forms", tags=["Forms"])
