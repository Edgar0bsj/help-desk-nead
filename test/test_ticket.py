import pytest  # noqa: F401

from module.ticket.ticket_facade import get_tickets_user, ticket_save


# @pytest.mark.skip(
#     reason="Funcionalidade em desenvolvimento, será ativada na próxima sprint."
# )
def test_created():
    ticket_save(
        produto="PRESENCIAL",
        titulo="Não sei aonde é a faculdade",
        descricao="cade a faculdade?",
        fk_user_id="user_HGRGe_ckD242KQpl",
        numero="21912345678",
    )
    ticket_save(
        produto="SEMI_PRESENCIAL",
        titulo="Prova não abre",
        descricao="cade a minha prova",
        fk_user_id="user_HGRGe_ckD242KQpl",
        numero="21912345678",
    )


def test_find_all_tickets():
    tickets = get_tickets_user("user_QRlXeJ2t73pts0L-")
    print(tickets)
