from sqlalchemy import Column,Table, Integer, DateTime, String,ForeignKey
from sqlalchemy.orm import relationship

from core.base import Base


class ArchivoTarea(Base):
    __tablename__ = "archivos_tareas"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(500), nullable=True)
    tipo = Column(String(20), nullable=False)
    ruta = Column(String(500), nullable=False)

    tarea_id = Column(Integer, ForeignKey("tareas.id"), nullable=False)
    tareas = relationship(
        "Tarea",
        back_populates="archivos_tareas"
    )
    
