from fastapi import APIRouter
from app.modules.identity_osint import search_identity

router = APIRouter()

@router.get("/identity/{query}")
def identity(query: str):
    return search_identity(query)