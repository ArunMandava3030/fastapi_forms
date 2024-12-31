from sqlmodel import SQLModel, Field
from typing import List, Dict, Optional
import uuid

class Form(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    title: str
    description: str
    fields: List[Dict]

class FormSubmission(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    form_id: str
    responses: Dict
    submitted_at: Optional[str]
