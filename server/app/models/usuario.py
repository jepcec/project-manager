from sqlalchemy import Column, Integer, String,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from core.base import Base
from models.proyecto import proyecto_usuarios
from models.tarea import tarea_usuarios

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String(500))
    email = Column(String(500))
    password = Column(String(500))
    telefono = Column(Integer)
    es_admin = Column(Boolean, default=False)

    proyectos = relationship(
        "Proyecto",
        secondary=proyecto_usuarios,
        back_populates="usuarios"
    )

    tareas = relationship(
        "Tarea",
        secondary=tarea_usuarios,
        back_populates="usuarios"
    )


