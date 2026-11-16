from nanoid import generate

from module.ticket.ticket_dto import TicketDTO
from module.ticket.user_cases import TicketLoad
from module.user.user_facade import get_user

ticket_ctrl = TicketLoad()


def ticket_save(
    produto: str,
    titulo: str,
    descricao: str,
    fk_user_id: str,
    numero: str,
):
    try:
        user = get_user(fk_user_id)

        if not user:
            return

        ticket_id = generate(size=7)
        ticket_dto = TicketDTO(
            id=ticket_id,
            produto=produto,
            titulo=titulo,
            descricao=descricao,
            fk_user_id=fk_user_id,
            numero=numero,
            status="OPEN",
        )

        ticket_ctrl.created(ticket_dto)

    except Exception as err:
        print(err)
        raise


def get_tickets_user(user_id: str) -> list[TicketDTO]:
    tickets = ticket_ctrl.find_all(fk_user_id=user_id)
    return tickets
