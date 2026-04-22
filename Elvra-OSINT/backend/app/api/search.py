from fastapi import APIRouter
from app.modules.search_builder import build_query

router = APIRouter()

@router.post("/search")
def search(data: dict):
    query = build_query(data)
    return {"query": query}