from fastapi import APIRouter
from core.db import test_connection

router = APIRouter()


@router.get("/health-db")
def health_db():
    response = test_connection()
    return {"status": response}