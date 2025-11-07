from sqlalchemy import Column,Table, Integer, DateTime, String,ForeignKey
from sqlalchemy.orm import relationship

from core.base import Base

class ArchivoProyecto(Base):
    __tablename__ = "archivos_proyectos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(500), nullable=True)
    tipo = Column(String(20), nullable=False)
    ruta = Column(String(500), nullable=False)