import os
from typing import Union
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from core.db import init_db, engine


@asynccontextmanager
async def lifespan(app:FastAPI):
    """
    Gestion del ciclo de vida de app
    """
    print("[1] start app")
    init_db()
    upload_dir = os.getenv("UPLOAD_DIR", "./uploads")
    os.makedirs(upload_dir, exist_ok=True)
    os.makedirs(f"{upload_dir}/proyectos", exist_ok=True)
    os.makedirs(f"{upload_dir}/tareas", exist_ok=True)
    print("✓ Directorios de archivos creados")
    
    yield
    
    # Shutdown
    print("[2] Cerrando aplicación...")
    engine.dispose()

    
app = FastAPI(
    title="Sistema de Administración de Proyectos",
    description="API REST para gestión de proyectos, tareas y usuarios",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)


@app.get("/info")
async def root():
    """
    ruta raiz
    """
    return {
        "message":"Api sistema de de administracion de archivos"
    }

