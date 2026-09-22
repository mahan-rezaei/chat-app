from fastapi import APIRouter, status
from dependencies import SessionDep
from schemas.users import UserCreate


router = APIRouter(prefix="/users")


@router.post('/register', status_code=status.HTTP_200_OK)
async def register_user(user: UserCreate, session: SessionDep):
    pass