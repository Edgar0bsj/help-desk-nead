from fastapi import APIRouter, Cookie, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/user", tags=["Usuario"])
templates = Jinja2Templates(directory="public")

from module.user.user_facade import (
    get_user_perfil,
    user_token_content,
)


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

    user = get_user_perfil(user_id)

    return templates.TemplateResponse(
        request=request,
        name="ticket.html",
        context={
            "user": {
                "name": user.name,
                "email": user.email,
                "role": user.role,
                "perfil": user.perfil,
            }
        },
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
        context={},
    )
