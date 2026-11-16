from sqlalchemy.orm import Session, sessionmaker

from module.ticket.ticket_dto import TicketDTO
from module.ticket.ticket_model import TickerModel


class TicketAlteration:
    SessionLocal: sessionmaker[Session]

    def __init__(self):
        pass

    def created(self, ticket_dto: TicketDTO) -> None:

        ticket_dto = ticket_dto.model_dump()
        model = TickerModel(**ticket_dto)

        with self.SessionLocal() as session:
            session.add(model)
            session.commit()

            session.refresh(model)

            return model

    def updated(self, ticket_dto: TicketDTO) -> None:

        if ticket_dto.id is None:
            return None

        with self.SessionLocal() as session:
            ticket = session.get(TickerModel, ticket_dto.id)

            ticket.produto = ticket_dto.produto
            ticket.titulo = ticket_dto.titulo
            ticket.descricao = ticket_dto.descricao
            ticket.status = ticket_dto.status
            ticket.numero = ticket_dto.numero

            session.commit()
            session.refresh(ticket)

            return ticket

    def deleted(self, id: str) -> bool:

        with self.SessionLocal() as session:
            ticket = session.get(TickerModel, id)

            if not ticket:
                return False

            session.delete(ticket)
            session.commit()

            return True
