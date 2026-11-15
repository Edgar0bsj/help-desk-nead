from jose import ExpiredSignatureError, JWTError, jwt
from nanoid import generate

from module.user.user_cases import UserLoad
from module.user.user_dto import UserDTO

user_ctrl = UserLoad()


def user_authentication(email: str, password: str) -> str | None:
    try:
        user = user_ctrl.find_by_email(email)

        if user is None:
            return None

        is_password = user_ctrl.password_validation(password, user.password)
        if not is_password:
            return None

        access_token = user_ctrl.make_token_generation(
            {"user_id": user.id, "perfil": user.perfil}
        )
        return access_token

    except Exception as err:
        print(err)
        raise


def user_token_content(token: str) -> tuple[str, str] | None:

    try:
        token = token.replace("Bearer ", "")
        payload = jwt.decode(
            token, user_ctrl.SECRET_KEY, algorithms=[user_ctrl.ALGORITHM]
        )
        user_id: str = payload.get("user_id")
        user_perfil: str = payload.get("perfil")

        if user_id is None:
            return None

        return (user_id, user_perfil)

    except ExpiredSignatureError:
        # ESSE É O ERRO ESPECÍFICO DE TOKEN EXPIRADO!
        return (None, None)
    except JWTError as err:
        print(err)
        raise


def user_save(
    name: str,
    cpf: str,
    email: str,
    password: str,
    role: str,
    perfil: str,
):
    try:
        id = generate(size=16)
        user_id = f"user_{id}"
        user_password = user_ctrl.make_password_hash(password)
        user_dto = UserDTO(
            id=user_id,
            name=name,
            cpf=cpf,
            email=email,
            password=user_password,
            role=role,
            perfil=perfil,
        )

        user_ctrl.created(user_dto)

    except Exception as err:
        print(err)
        raise


def get_user_perfil(id: str):
    user = user_ctrl.find_by_id(id)

    user.name = user.name.title()

    nome_list = user.name.split()
    iniciais = "".join(e[0] for e in nome_list)

    user.perfil = iniciais[:2]

    return user
