from fastapi import APIRouter, Form, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/auth", tags=["Auth"])
templates = Jinja2Templates(directory="public")

from module.user.user_facade import (
    user_authentication,
)


@router.get("/login", name="login")
async def auth_login(request: Request, err: bool | None = None):

    return templates.TemplateResponse(
        request=request,
        name="auth-login.html",
        context={"error": err},
    )


@router.get("/logout", name="logout")
async def auth_logout():
    response = RedirectResponse(
        url="/auth/login/", status_code=status.HTTP_303_SEE_OTHER
    )

    response.delete_cookie(key="access_token")

    return response


@router.post("/authentication", name="authentication")
async def authentication(
    request: Request, email: str = Form(...), password: str = Form(...)
):

    token = user_authentication(email, password)

    if token is None:
        return RedirectResponse(
            url="/auth/login/?err=true", status_code=status.HTTP_303_SEE_OTHER
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
