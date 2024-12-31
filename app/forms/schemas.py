from pydantic import BaseModel
from typing import List, Dict

class FormCreate(BaseModel):
    title: str
    description: str
    fields: List[Dict]

class FormSubmission(BaseModel):
    responses: List[Dict]
