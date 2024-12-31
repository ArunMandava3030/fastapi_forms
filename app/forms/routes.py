from fastapi import APIRouter, Depends
from app.forms.schemas import FormCreate, FormSubmission
from app.forms.utils import (
    create_form,
    delete_form,
    get_all_forms,
    get_form_by_id,
    submit_form,
    get_form_submissions,
)
from app.database import get_session

router = APIRouter()

@router.post("/create")
async def create(form: FormCreate, session=Depends(get_session)):
    return await create_form(form, session)

@router.delete("/delete/{form_id}")
async def delete(form_id: str, session=Depends(get_session)):
    await delete_form(form_id, session)
    return {"message": "Form deleted successfully"}

@router.get("/")
async def all_forms(session=Depends(get_session)):
    return await get_all_forms(session)

@router.get("/{form_id}")
async def single_form(form_id: str, session=Depends(get_session)):
    return await get_form_by_id(form_id, session)

@router.post("/submit/{form_id}")
async def submit(form_id: str, submission: FormSubmission, session=Depends(get_session)):
    return await submit_form(form_id, submission, session)

@router.get("/submissions/{form_id}")
async def submissions(form_id: str, page: int = 1, limit: int = 10, session=Depends(get_session)):
    return await get_form_submissions(form_id, page, limit, session)
