"""
Schemas Pydantic para validación de datos
Sistema de Administración de Proyectos
"""

from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional, List
from datetime import date, datetime
from enum import Enum


# ============================================
# ENUMS
# ============================================

class EstadoTareaEnum(str, Enum):
    pendiente = "pendiente"
    en_progreso = "en_progreso"
    completada = "completada"
    cancelada = "cancelada"


class TipoArchivoEnum(str, Enum):
    pdf = "pdf"
    doc = "doc"
    docx = "docx"
    jpg = "jpg"
    jpeg = "jpeg"


# ============================================
# SCHEMAS DE USUARIO
# ============================================

class UsuarioBase(BaseModel):
    nombre_completo: str = Field(..., min_length=3, max_length=200)
    email: EmailStr
    telefono: Optional[str] = Field(None, max_length=20)
    estado: bool = True
    es_administrador: bool = False


class UsuarioCreate(UsuarioBase):
    password: str = Field(..., min_length=8, max_length=100)
    
    @field_validator('password')
    def validar_password(cls, v):
        if not any(char.isdigit() for char in v):
            raise ValueError('La contraseña debe contener al menos un número')
        if not any(char.isupper() for char in v):
            raise ValueError('La contraseña debe contener al menos una mayúscula')
        if not any(char.islower() for char in v):
            raise ValueError('La contraseña debe contener al menos una minúscula')
        return v


class UsuarioUpdate(BaseModel):
    nombre_completo: Optional[str] = Field(None, min_length=3, max_length=200)
    email: Optional[EmailStr] = None
    telefono: Optional[str] = Field(None, max_length=20)
    estado: Optional[bool] = None
    es_administrador: Optional[bool] = None


class UsuarioPasswordUpdate(BaseModel):
    password_actual: str
    password_nueva: str = Field(..., min_length=8, max_length=100)
    
    @field_validator('password_nueva')
    def validar_password(cls, v):
        if not any(char.isdigit() for char in v):
            raise ValueError('La contraseña debe contener al menos un número')
        if not any(char.isupper() for char in v):
            raise ValueError('La contraseña debe contener al menos una mayúscula')
        if not any(char.islower() for char in v):
            raise ValueError('La contraseña debe contener al menos una minúscula')
        return v


class UsuarioResponse(UsuarioBase):
    id: int
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    
    class Config:
        from_attributes = True


# ============================================
# SCHEMAS DE AUTENTICACIÓN
# ============================================

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    usuario: UsuarioResponse


# ============================================
# SCHEMAS DE PROYECTO
# ============================================

class ProyectoBase(BaseModel):
    titulo: str = Field(..., min_length=5, max_length=300)
    descripcion: Optional[str] = None
    fecha_inicio: date
    fecha_finalizacion: date
    
    @field_validator('fecha_finalizacion')
    def validar_fechas(cls, v, values):
        if 'fecha_inicio' in values and v < values['fecha_inicio']:
            raise ValueError('La fecha de finalización debe ser posterior a la fecha de inicio')
        return v


class ProyectoCreate(ProyectoBase):
    responsables_ids: Optional[List[int]] = []


class ProyectoUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=5, max_length=300)
    descripcion: Optional[str] = None
    fecha_inicio: Optional[date] = None
    fecha_finalizacion: Optional[date] = None


class ResponsableProyectoResponse(BaseModel):
    id: int
    nombre_completo: str
    email: str
    fecha_asignacion: datetime
    
    class Config:
        from_attributes = True


class ProyectoResponse(ProyectoBase):
    id: int
    creado_por: int
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    responsables: List[ResponsableProyectoResponse] = []
    
    class Config:
        from_attributes = True


class ProyectoDetalle(ProyectoResponse):
    total_tareas: int = 0
    tareas_completadas: int = 0
    tareas_en_progreso: int = 0
    tareas_pendientes: int = 0
    total_archivos: int = 0


# ============================================
# SCHEMAS DE TAREA
# ============================================

class TareaBase(BaseModel):
    titulo: str = Field(..., min_length=5, max_length=300)
    descripcion: Optional[str] = None
    fecha_inicio: date
    fecha_finalizacion: date
    
    @field_validator('fecha_finalizacion')
    def validar_fechas(cls, v, values):
        if 'fecha_inicio' in values and v < values['fecha_inicio']:
            raise ValueError('La fecha de finalización debe ser posterior a la fecha de inicio')
        return v


class TareaCreate(TareaBase):
    proyecto_id: int
    usuario_asignado_id: int


class TareaUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=5, max_length=300)
    descripcion: Optional[str] = None
    fecha_inicio: Optional[date] = None
    fecha_finalizacion: Optional[date] = None
    usuario_asignado_id: Optional[int] = None
    estado: Optional[EstadoTareaEnum] = None


class TareaResponse(TareaBase):
    id: int
    proyecto_id: int
    usuario_asignado_id: int
    estado: EstadoTareaEnum
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    
    class Config:
        from_attributes = True


class TareaDetalle(TareaResponse):
    proyecto_titulo: Optional[str] = None
    usuario_asignado_nombre: Optional[str] = None
    total_archivos: int = 0


# ============================================
# SCHEMAS DE ARCHIVO
# ============================================

class ArchivoBase(BaseModel):
    nombre_archivo: str = Field(..., max_length=255)
    tipo_archivo: TipoArchivoEnum
    tamano_bytes: Optional[int] = None


class ArchivoProyectoCreate(ArchivoBase):
    proyecto_id: int
    ruta_archivo: str


class ArchivoTareaCreate(ArchivoBase):
    tarea_id: int
    ruta_archivo: str


class ArchivoProyectoResponse(ArchivoBase):
    id: int
    proyecto_id: int
    ruta_archivo: str
    subido_por: int
    fecha_subida: datetime
    
    class Config:
        from_attributes = True


class ArchivoTareaResponse(ArchivoBase):
    id: int
    tarea_id: int
    ruta_archivo: str
    subido_por: int
    fecha_subida: datetime
    
    class Config:
        from_attributes = True


# ============================================
# SCHEMAS DE LOG
# ============================================

class LogActividadCreate(BaseModel):
    usuario_id: Optional[int] = None
    accion: str = Field(..., max_length=100)
    entidad_tipo: str
    entidad_id: int
    descripcion: Optional[str] = None
    ip_address: Optional[str] = Field(None, max_length=45)


class LogActividadResponse(BaseModel):
    id: int
    usuario_id: Optional[int] = None
    accion: str
    entidad_tipo: str
    entidad_id: int
    descripcion: Optional[str] = None
    ip_address: Optional[str] = None
    fecha_hora: datetime
    
    class Config:
        from_attributes = True


# ============================================
# SCHEMAS PARA FILTROS Y BÚSQUEDA
# ============================================

class FiltroProyectos(BaseModel):
    titulo: Optional[str] = None
    fecha_inicio_desde: Optional[date] = None
    fecha_inicio_hasta: Optional[date] = None
    responsable_id: Optional[int] = None
    page: int = Field(1, ge=1)
    page_size: int = Field(10, ge=1, le=100)


class FiltroTareas(BaseModel):
    titulo: Optional[str] = None
    proyecto_id: Optional[int] = None
    usuario_asignado_id: Optional[int] = None
    estado: Optional[EstadoTareaEnum] = None
    fecha_inicio_desde: Optional[date] = None
    fecha_inicio_hasta: Optional[date] = None
    page: int = Field(1, ge=1)
    page_size: int = Field(10, ge=1, le=100)


class FiltroUsuarios(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    estado: Optional[bool] = None
    es_administrador: Optional[bool] = None
    page: int = Field(1, ge=1)
    page_size: int = Field(10, ge=1, le=100)


# ============================================
# SCHEMAS DE RESPUESTAS PAGINADAS
# ============================================

class PaginatedResponse(BaseModel):
    total: int
    page: int
    page_size: int
    total_pages: int
    data: List


class ProyectosPaginados(PaginatedResponse):
    data: List[ProyectoResponse]


class TareasPaginadas(PaginatedResponse):
    data: List[TareaResponse]


class UsuariosPaginados(PaginatedResponse):
    data: List[UsuarioResponse]


# ============================================
# SCHEMAS DE ESTADÍSTICAS
# ============================================

class EstadisticasUsuario(BaseModel):
    total_proyectos_responsable: int
    total_tareas_asignadas: int
    tareas_completadas: int
    tareas_pendientes: int
    tareas_en_progreso: int


class EstadisticasGenerales(BaseModel):
    total_usuarios: int
    usuarios_activos: int
    total_proyectos: int
    total_tareas: int
    tareas_completadas: int
    tareas_pendientes: int


# ============================================
# SCHEMAS DE RESPUESTA GENÉRICA
# ============================================

class MessageResponse(BaseModel):
    message: str
    success: bool = True


class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None
    success: bool = False