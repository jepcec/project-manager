from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime, func
from sqlalchemy.orm import relationship
from core.base import Base
proyecto_usuarios = Table(
    "proyecto_usuarios", 
    Base.metadata,
    Column("id_proyecto",Integer, ForeignKey("proyectos.id"), primary_key=True),
    Column("id_usuario", Integer, ForeignKey("usuarios.id"), primary_key=True),
    Column("id_rol", Integer, ForeignKey("roles.id"))
)


class Proyecto(Base):
    __tablename__ = "proyectos"
    id = Column(Integer, primary_key=True)
    titulo_proyecto = Column(String(500), nullable=False)
    descripcion = Column(String(500), nullable=True)
    fecha_inicio = Column(DateTime(timezone=True), nullable=True)
    fecha_fin = Column(DateTime, nullable=True)


    usuarios = relationship(
        "Usuario",
        secondary=proyecto_usuarios,
        back_populates="proyectos"
    )

    tareas = relationship(
        "Tarea",
        back_populates="proyectos"
    )

    archivos_proyectos = relationship(
        "ArchivoProyecto",
        back_populates="proyectos"
    )
