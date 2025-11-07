from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import usuario
from models import Usuario
from core.db import get_db
router = APIRouter()

@router.post("/t-crear",response_model=usuario.UsuarioBase)
def crear_usuario(usuario: usuario.UsuarioCrear, db: Session = Depends(get_db)):
    db_usuario = Usuario(nombre_completo = usuario.nombre_completo, email = usuario.email, password = usuario.password,telefono = usuario.telefono, es_admin = usuario.es_admin)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario