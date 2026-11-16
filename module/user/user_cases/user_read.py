from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from module.user.user_dto import UserDTO
from module.user.user_model import UserModel


class UserRead:
    SessionLocal: sessionmaker[Session]

    def __init__(self):
        pass

    def find_all(
        self,
        name: str | None = None,
        cpf: str | None = None,
        email: str | None = None,
        role: str | None = None,
        perfil: str | None = None,
    ) -> list[UserDTO]:

        with self.SessionLocal() as session:
            statement = select(UserModel)

            if name:
                statement = statement.where(UserModel.name.ilike(f"%{name}%"))

            if cpf:
                statement = statement.where(UserModel.cpf.ilike(f"%{cpf}%"))

            if email:
                statement = statement.where(UserModel.email.ilike(f"%{email}%"))

            if role:
                statement = statement.where(UserModel.role.ilike(f"%{role}%"))

            if perfil:
                statement = statement.where(UserModel.perfil.ilike(f"%{perfil}%"))

            user = session.scalars(statement).all()

            buffer = [
                UserDTO(
                    id=e.id,
                    name=e.name,
                    cpf=e.cpf,
                    email=e.email,
                    password=e.password,
                    role=e.role,
                    perfil=e.perfil,
                )
                for e in user
            ]

            return buffer

    def find_by_id(self, id: str):

        with self.SessionLocal() as session:
            user = session.get(UserModel, id)

        if user is None:
            return None

        user_dto = UserDTO(
            id=user.id,
            name=user.name,
            cpf=user.cpf,
            email=user.email,
            password=user.password,
            role=user.role,
            perfil=user.perfil,
        )
        return user_dto

    def find_by_email(self, email: str) -> UserDTO | None:

        with self.SessionLocal() as session:
            statement = select(UserModel).where(UserModel.email == email)
            user = session.execute(statement).scalar_one_or_none()

            if user:
                user = UserDTO(
                    id=user.id,
                    name=user.name,
                    cpf=user.cpf,
                    email=user.email,
                    password=user.password,
                    role=user.role,
                    perfil=user.perfil,
                )

            return user
