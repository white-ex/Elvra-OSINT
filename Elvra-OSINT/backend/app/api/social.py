from fastapi import APIRouter
from app.modules.username_check import check_username

router = APIRouter()

@router.get("/socials/{username}")
def socials(username: str):

    return {
        "username": username,
        "profiles": check_username(username)
    }