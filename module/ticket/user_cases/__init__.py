from module.ticket.user_cases.ticket_alteration import TicketAlteration
from module.ticket.user_cases.ticket_init import TicketInit
from module.ticket.user_cases.ticket_read import TicketRead


class TicketLoad(TicketRead, TicketInit, TicketAlteration):
    def __init__(self):
        TicketInit.__init__(self)
        TicketAlteration.__init__(self)
        TicketRead.__init__(self)
