from fastapi import APIRouter

router = APIRouter()

@router.post("/chatbot")
def chatbot():
    return {
        "reply": "Please visit the nearest police station and file a complaint. Medical examination should be conducted as per legal procedure."
    }