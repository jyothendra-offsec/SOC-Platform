from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Welcome to the Enterprise SOC Platform",
        "version": "0.1.0",
        "status": "running"
        }
