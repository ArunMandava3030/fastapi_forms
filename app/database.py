from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql://user:password@localhost/fastapi_forms"

engine = create_engine(DATABASE_URL)

async def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
