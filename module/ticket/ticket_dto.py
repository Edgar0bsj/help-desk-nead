from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, Field


class StatusType(StrEnum):
    OPEN = "OPEN"
    EM_PROCESSO = "EM_PROCESSO"
    RESOLVIDO = "RESOLVIDO"
    CANCELADO = "CANCELADO"


class ProdutoType(StrEnum):
    EAD = "EAD"
    SEMI_PRESENCIAL = "SEMI_PRESENCIAL"
    PRESENCIAL = "PRESENCIAL"


id_type = Annotated[str, Field(max_length=50)]
titulo_type = Annotated[str, Field(max_length=225)]
descricao_type = Annotated[str, Field(max_length=400)]
fk_user_id_type = Annotated[str, Field(max_length=50)]
numero_type = Annotated[str, Field(max_length=25)]


class TicketDTO(BaseModel):
    id: id_type | None
    produto: ProdutoType
    titulo: titulo_type
    descricao: descricao_type
    fk_user_id: fk_user_id_type
    status: StatusType
    numero: numero_type
