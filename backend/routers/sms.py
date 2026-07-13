from fastapi import APIRouter

router = APIRouter()

@router.post("/send-sms")
def send_sms():
    return {
        "message": "SMS Alert Sent Successfully"
    }