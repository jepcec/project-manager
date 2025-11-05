import os
from fastapi import FastAPI

# ============================= ROUTES ============================
from routes import health
# =================================================================
app = FastAPI()
app.include_router(health.router)


