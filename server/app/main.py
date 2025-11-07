"""
    PROGRAMA PRINCIPAL 
"""
import os
from fastapi import FastAPI
from core.db import engine

app = FastAPI()

# ============================= ROUTES ============================
from routes import health, usuario
app.include_router(health.router)
app.include_router(usuario.router)

# ============================ MODELOS ============================
from models import *
from core.base import Base

Base.metadata.create_all(bind=engine)



