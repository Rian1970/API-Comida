from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional

# Esquema Pydantic para crear
class ClienteSchema(BaseModel):
    nombre: str = Field(min_length=2, max_length=50)
    telefono: str = Field(min_length=10, max_length=15)
    correo: EmailStr = Field(max_length=50)
    contrasenia: str = Field(min_length=8, max_length=50)

    model_config = {
        "json_schema_extra": {
            "example": {
                "nombre": "Diego",
                "telefono": "5512657390",
                "correo": "diegod@gmail.com",
                "contrasenia": "MiC0ntra5eni@"
            }
        }
    }

# Esquema Pydantic para actualizar
class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None
    telefono: Optional[str] = None
    contrasenia: Optional[str] = None

    model_config = {
        'json_schema_extra' : {
            "example": {
                "nombre": "Diego",
                "telefono": "5512657390",
                "correo": "diegod@gmail.com",
                "contrasenia": "MiC0ntra5eni@"
            }
        }
    }