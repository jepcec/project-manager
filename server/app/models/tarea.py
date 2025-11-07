from sqlalchemy import Column,Table, Integer, DateTime, String,ForeignKey
from sqlalchemy.orm import relationship

from core.base import Base

tarea_usuarios = Table(
    "tarea_usuarios",
    Base.metadata,
    Column("id_tarea", Integer,ForeignKey("tareas.id"), primary_key=True),
    Column("id_usuario", Integer, ForeignKey("usuarios.id"), primary_key=True),
    Column("id_rol", Integer, ForeignKey("roles.id"))
)


class Tarea(Base):
    __tablename__ = "tareas"
    id = Column(Integer, primary_key=True, nullable=False)
    titulo = Column(String(500), nullable=False)
    descripcion = Column(String(500), nullable=True)
    fecha_inicio = Column(DateTime(timezone=True), nullable=True)
    fecha_fin = Column(DateTime, nullable=True)
    id_proyecto = Column(Integer, ForeignKey("proyectos.id"))
    
    usuarios = relationship(
        "Usuario",
        secondary=tarea_usuarios,
        back_populates="tareas"
    )

    proyectos = relationship(
        "Proyecto",
        back_populates="tareas"
    )

    archivos_tareas = relationship(
        "ArchivoTarea",
        back_populates="tareas"
    )
