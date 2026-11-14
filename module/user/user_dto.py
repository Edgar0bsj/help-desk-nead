from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, Field, field_validator


class RoleType(StrEnum):
    ADMINISTRADOR = "admin"
    PROFESSOR = "professor"
    COORDENADOR = "coordenador"
    PROF_COORD = "prof_coordenador"
    RELACIONAMENTO = "relacionamento"
    CONTABILIDADE = "contabilidade"
    SECRETARIA = "secretaria"


class PerfilType(StrEnum):
    USUARIO = "user"
    ADMINISTRADOR = "admin"


id_type = Annotated[str, Field(max_length=50)]
name_type = Annotated[str, Field(max_length=50)]
cpf_type = Annotated[str, Field(max_length=11)]
email_type = Annotated[str, Field(max_length=50)]


class UserDTO(BaseModel):
    id: id_type | None
    name: name_type
    cpf: cpf_type
    email: email_type
    password: str
    role: RoleType
    perfil: PerfilType

    @field_validator("name", mode="after")
    @classmethod
    def normalizar_name(cls, value: str) -> str:
        return value.strip().lower()
