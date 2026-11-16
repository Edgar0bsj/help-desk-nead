from fastapi import APIRouter, Cookie, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from module.ticket.ticket_facade import get_tickets_user
from module.user.user_facade import (
    user_token_content,
)

router = APIRouter(prefix="/user", tags=["Usuario"])
templates = Jinja2Templates(directory="public")


@router.get("/ticket", name="ticket")
async def user_ticket(
    request: Request, access_token: str | None = Cookie(default=None)
):
    if access_token is None:
        return RedirectResponse(
            url="/auth/login/?err=true", status_code=status.HTTP_303_SEE_OTHER
        )

    user_id, user_perfil = user_token_content(access_token)

    if (user_id is None) or (user_perfil is None):
        return RedirectResponse(
            url="/auth/login/", status_code=status.HTTP_303_SEE_OTHER
        )

    tickets = get_tickets_user(user_id)

    return templates.TemplateResponse(
        request=request,
        name="ticket.html",
        context={"tickets": tickets},
    )


@router.get("/add-ticket", name="add-ticket")
async def user_add_ticket(
    request: Request, access_token: str | None = Cookie(default=None)
):
    if access_token is None:
        return RedirectResponse(
            url="/auth/login/?err=true", status_code=status.HTTP_303_SEE_OTHER
        )

    user_id, user_perfil = user_token_content(access_token)

    if (user_id is None) or (user_perfil is None):
        return RedirectResponse(
            url="/auth/login/", status_code=status.HTTP_303_SEE_OTHER
        )

    return templates.TemplateResponse(
        request=request,
        name="add_ticket_form.html",
        context={"user_id": user_id},
    )
