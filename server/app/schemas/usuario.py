from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioBase(BaseModel):
    nombre_completo: str
    email: EmailStr
    password: str
    telefono: Optional[int] = None 
    es_admin: bool = False



class UsuarioCrear(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    id: int
    class Config:
        orm_model = True
        