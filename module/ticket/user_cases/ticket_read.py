from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from module.ticket.ticket_dto import TicketDTO
from module.ticket.ticket_model import TickerModel


class TicketRead:
    SessionLocal: sessionmaker[Session]

    def __init__(self):
        pass

    def find_all(
        self,
        produto: str | None = None,
        titulo: str | None = None,
        descricao: str | None = None,
        fk_user_id: str | None = None,
        status: str | None = None,
        numero: str | None = None,
    ) -> list[TicketDTO]:

        with self.SessionLocal() as session:
            statement = select(TickerModel)

            if produto:
                statement = statement.where(TickerModel.produto.ilike(f"%{produto}%"))

            if titulo:
                statement = statement.where(TickerModel.titulo.ilike(f"%{titulo}%"))

            if descricao:
                statement = statement.where(
                    TickerModel.descricao.ilike(f"%{descricao}%")
                )

            if fk_user_id:
                statement = statement.where(
                    TickerModel.fk_user_id.ilike(f"%{fk_user_id}%")
                )

            if numero:
                statement = statement.where(TickerModel.numero.ilike(f"%{numero}%"))

            if status:
                statement = statement.where(TickerModel.status.ilike(f"%{status}%"))

            ticket = session.scalars(statement).all()

            buffer = [
                TicketDTO(
                    id=e.id,
                    produto=e.produto,
                    titulo=e.titulo,
                    descricao=e.descricao,
                    fk_user_id=e.fk_user_id,
                    status=e.status,
                    numero=e.numero,
                )
                for e in ticket
            ]

            return buffer

    def find_by_id(self, id: str):

        with self.SessionLocal() as session:
            ticket = session.get(TickerModel, id)

        if ticket is None:
            return None

        ticket_dto = TicketDTO(
            id=ticket.id,
            produto=ticket.produto,
            titulo=ticket.titulo,
            descricao=ticket.descricao,
            fk_user_id=ticket.fk_user_id,
            status=ticket.status,
            numero=ticket.numero,
        )
        return ticket_dto
