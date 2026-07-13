from fastapi import FastAPI

# Import all routers
from routers.auth import router as auth_router
from routers.case import router as case_router
from routers.dashboard import router as dashboard_router
from routers.chatbot import router as chatbot_router
from routers.sms import router as sms_router

app = FastAPI(
    title="SAKSHI Backend",
    description="Procedural Accountability Platform for POCSO Cases",
    version="1.0.0"
)

# Home API
@app.get("/")
def home():
    return {
        "message": "Welcome to SAKSHI Backend 🚀"
    }

# Register all routers
app.include_router(auth_router)
app.include_router(case_router)
app.include_router(dashboard_router)
app.include_router(chatbot_router)
app.include_router(sms_router)