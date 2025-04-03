from fastapi import APIRouter
from backend.ai.model.interest import Interest


interests_router = APIRouter(prefix="/interests")

@interests_router.get("/")
async def get_interests() -> list[str]:
    interests = [interest.value for interest in Interest]
    return interests