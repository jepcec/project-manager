from sqlalchemy import Column, Integer, String, Boolean, Text, Date, DateTime, Enum, ForeignKey, BigInteger, CheckConstraint, UniqueConstraint, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
import enum

from core.db import base


# ====================================
# ENUMS
# ====================================


class EstadoTarea(str,enum.Enum):
    pendiente = "pendiente"
    en_progreso = "en_progreso"
    completada = "completada"
    cancelada = "cancelada"

class TipoArchivo(str,enum.Enum):
    pdf = "pdf"
    doc = "doc"
    docx = "docx"
    jpg = "jpg"
    jpeg = "jpeg"

class EntidadTipo(str, enum.Enum):
    usuario = "usuario"
    proyecto = "proyecto"
    tarea = "tarea"


# ====================================
# MODELOS
# ====================================

class Usuario(base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre_completo = Column(String(200), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    telefono = Column(String(20), nullable=True)
    estado = Column(Boolean, default=True, nullable=False, index=True)
    es_administrador = Column(Boolean, default=False, nullable=False)
    fecha_creacion = Column(DateTime, server_default=func.current_timestamp(), nullable=False)
    fecha_actualizacion = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)

    # Relaciones
    proyectos_creados = relationship("Proyecto", back_populates="creador", foreign_keys="Proyecto.creado_por")
    proyectos_responsable = relationship("ResponsableProyecto", back_populates="usuario")
    tareas_asignadas = relationship("Tarea", back_populates="usuario_asignado", foreign_keys="Tarea.usuario_asignado_id")
    archivos_proyecto_subidos = relationship("ArchivoProyecto", back_populates="subido_por_usuario")
    archivos_tarea_subidos = relationship("ArchivoTarea", back_populates="subido_por_usuario")
    logs = relationship("LogActividad", back_populates="usuario")

class Proyecto(base):
    __tablename__ = "proyectos"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(300), nullable=False)
    descripcion = Column(Text, nullable=True)
    fecha_inicio = Column(Date, nullable=False)
    fecha_finalizacion = Column(Date, nullable=False)
    creado_por = Column(Integer, ForeignKey("usuarios.id", ondelete="RESTRICT"), nullable=False, index=True)
    fecha_creacion = Column(DateTime, server_default=func.current_timestamp(), nullable=False)
    fecha_actualizacion = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)
    
    # Constraint
    __table_args__ = (
        CheckConstraint('fecha_finalizacion >= fecha_inicio', name='chk_fechas_proyecto'),
        Index('idx_fechas', 'fecha_inicio', 'fecha_finalizacion'),
    )
    
    # Relaciones
    creador = relationship("Usuario", back_populates="proyectos_creados", foreign_keys=[creado_por])
    responsables = relationship("ResponsableProyecto", back_populates="proyecto", cascade="all, delete-orphan")
    tareas = relationship("Tarea", back_populates="proyecto", cascade="all, delete-orphan")
    archivos = relationship("ArchivoProyecto", back_populates="proyecto", cascade="all, delete-orphan")

class ResponsableProyecto(base):
    __tablename__ = "responsables_proyecto"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    proyecto_id = Column(Integer, ForeignKey("proyectos.id", ondelete="CASCADE"), nullable=False, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False, index=True)
    fecha_asignacion = Column(DateTime, server_default=func.current_timestamp(), nullable=False)
    
    # Constraint
    __table_args__ = (
        UniqueConstraint('proyecto_id', 'usuario_id', name='unique_responsable'),
    )
    
    # Relaciones
    proyecto = relationship("Proyecto", back_populates="responsables")
    usuario = relationship("Usuario", back_populates="proyectos_responsable")

class Tarea(base):
    __tablename__ = "tareas"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(300), nullable=False)
    descripcion = Column(Text, nullable=True)
    fecha_inicio = Column(Date, nullable=False)
    fecha_finalizacion = Column(Date, nullable=False)
    proyecto_id = Column(Integer, ForeignKey("proyectos.id", ondelete="CASCADE"), nullable=False, index=True)
    usuario_asignado_id = Column(Integer, ForeignKey("usuarios.id", ondelete="RESTRICT"), nullable=False, index=True)
    estado = Column(Enum(EstadoTarea), default=EstadoTarea.pendiente, nullable=False, index=True)
    fecha_creacion = Column(DateTime, server_default=func.current_timestamp(), nullable=False)
    fecha_actualizacion = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)
    
    # Constraint
    __table_args__ = (
        CheckConstraint('fecha_finalizacion >= fecha_inicio', name='chk_fechas_tarea'),
        Index('idx_fechas', 'fecha_inicio', 'fecha_finalizacion'),
    )
    
    # Relaciones
    proyecto = relationship("Proyecto", back_populates="tareas")
    usuario_asignado = relationship("Usuario", back_populates="tareas_asignadas", foreign_keys=[usuario_asignado_id])
    archivos = relationship("ArchivoTarea", back_populates="tarea", cascade="all, delete-orphan")

class ArchivoProyecto(base):
    __tablename__ = "archivos_proyecto"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    proyecto_id = Column(Integer, ForeignKey("proyectos.id", ondelete="CASCADE"), nullable=False, index=True)
    nombre_archivo = Column(String(255), nullable=False)
    ruta_archivo = Column(String(500), nullable=False)
    tipo_archivo = Column(Enum(TipoArchivo), nullable=False, index=True)
    tamano_bytes = Column(BigInteger, nullable=True)
    subido_por = Column(Integer, ForeignKey("usuarios.id", ondelete="RESTRICT"), nullable=False)
    fecha_subida = Column(DateTime, server_default=func.current_timestamp(), nullable=False)
    
    # Relaciones
    proyecto = relationship("Proyecto", back_populates="archivos")
    subido_por_usuario = relationship("Usuario", back_populates="archivos_proyecto_subidos")


class ArchivoTarea(base):
    __tablename__ = "archivos_tarea"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tarea_id = Column(Integer, ForeignKey("tareas.id", ondelete="CASCADE"), nullable=False, index=True)
    nombre_archivo = Column(String(255), nullable=False)
    ruta_archivo = Column(String(500), nullable=False)
    tipo_archivo = Column(Enum(TipoArchivo), nullable=False, index=True)
    tamano_bytes = Column(BigInteger, nullable=True)
    subido_por = Column(Integer, ForeignKey("usuarios.id", ondelete="RESTRICT"), nullable=False)
    fecha_subida = Column(DateTime, server_default=func.current_timestamp(), nullable=False)
    
    # Relaciones
    tarea = relationship("Tarea", back_populates="archivos")
    subido_por_usuario = relationship("Usuario", back_populates="archivos_tarea_subidos")


class LogActividad(base):
    __tablename__ = "logs_actividad"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="SET NULL"), nullable=True, index=True)
    accion = Column(String(100), nullable=False)
    entidad_tipo = Column(Enum(EntidadTipo), nullable=False, index=True)
    entidad_id = Column(Integer, nullable=False, index=True)
    descripcion = Column(Text, nullable=True)
    ip_address = Column(String(45), nullable=True)
    fecha_hora = Column(DateTime, server_default=func.current_timestamp(), nullable=False, index=True)
    
    # Relaciones
    usuario = relationship("Usuario", back_populates="logs")
