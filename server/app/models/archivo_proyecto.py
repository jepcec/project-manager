from sqlalchemy import Column,Table, Integer, DateTime, String,ForeignKey
from sqlalchemy.orm import relationship

from core.base import Base

class ArchivoProyecto(Base):
    __tablename__ = "archivos_proyectos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(500), nullable=True)
    tipo = Column(String(20), nullable=False)
    ruta = Column(String(500), nullable=False)

    proyecto_id = Column(Integer, ForeignKey("proyectos.id"), nullable=False)
    proyectos = relationship(
        "Proyecto",
        back_populates="archivos_proyectos"
    )