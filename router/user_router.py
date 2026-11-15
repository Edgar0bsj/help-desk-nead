from fastapi import APIRouter, Cookie, Form, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/user", tags=["Usuario"])
templates = Jinja2Templates(directory="public")

from module.user.user_facade import (
    get_user_perfil,
    user_authentication,
    user_token_content,
)


@router.get("/login", name="login")
async def user_login(request: Request, err: bool | None = None):

    return templates.TemplateResponse(
        request=request,
        name="auth-login.html",
        context={"error": err},
    )


@router.get("/logout", name="logout")
async def user_logout():
    response = RedirectResponse(
        url="/user/login/", status_code=status.HTTP_303_SEE_OTHER
    )

    response.delete_cookie(key="access_token")

    return response


@router.post("/user_auth", name="user_auth")
async def user_auth(
    request: Request, email: str = Form(...), password: str = Form(...)
):
    token = user_authentication(email, password)

    if token is None:
        return RedirectResponse(
            url="/user/login/?err=true", status_code=status.HTTP_303_SEE_OTHER
        )

    response = RedirectResponse(
        url="/user/ticket", status_code=status.HTTP_303_SEE_OTHER
    )

    response.set_cookie(
        key="access_token",
        value=f"Bearer {token}",
        httponly=True,
        secure=False,  # Mude para True se a aplicação usar HTTPS
        samesite="lax",
    )

    return response


@router.get("/ticket", name="ticket")
async def user_ticket(
    request: Request, access_token: str | None = Cookie(default=None)
):
    if access_token is None:
        return RedirectResponse(
            url="/user/login/?err=true", status_code=status.HTTP_303_SEE_OTHER
        )

    user_id, user_perfil = user_token_content(access_token)

    if (user_id is None) or (user_perfil is None):
        return RedirectResponse(
            url="/user/login/", status_code=status.HTTP_303_SEE_OTHER
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
