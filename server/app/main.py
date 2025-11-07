"""
    PROGRAMA PRINCIPAL 
"""
import os
from fastapi import FastAPI
from core.db import engine

app = FastAPI()

# ============================= ROUTES ============================
from routes import health
app.include_router(health.router)



from models import *
from core.base import Base

Base.metadata.create_all(bind=engine)



