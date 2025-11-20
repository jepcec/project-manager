"""
    PROGRAMA PRINCIPAL 
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.db import engine

app = FastAPI()
# ============================== CORS =============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ============================= ROUTES ============================
from routes import health, usuario
app.include_router(health.router)
app.include_router(usuario.router)

# ============================ MODELOS ============================
from models import *
from core.base import Base

Base.metadata.create_all(bind=engine)



