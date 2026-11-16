from fastapi import APIRouter, Cookie, Form, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from module.ticket.ticket_facade import ticket_save
from module.user.user_facade import (
    user_token_content,
)

router = APIRouter(prefix="/ticket", tags=["Ticket"])
templates = Jinja2Templates(directory="public")


@router.post("/new-ticket", name="new-ticket")
async def ticket_new(
    request: Request,
    access_token: str | None = Cookie(default=None),
    produto: str = Form(...),
    titulo: str = Form(...),
    descricao: str = Form(...),
    fk_user_id: str = Form(...),
    numero: str = Form(...),
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
    # -----
    result = ticket_save(
        titulo=titulo,
        produto=produto,
        descricao=descricao,
        numero=numero,
        fk_user_id=fk_user_id,
    )
    print(result)

    return RedirectResponse(url="/user/ticket", status_code=status.HTTP_303_SEE_OTHER)
