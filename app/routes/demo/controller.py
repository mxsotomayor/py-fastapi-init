from fastapi import APIRouter
router = APIRouter()

base_path = "/demo"

@router.get(f"{base_path}", tags=["Demo route"])
def demo_action():
    return {"message":"Hello demo"}