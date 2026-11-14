from sqlalchemy.orm import Session, sessionmaker

from module.user.user_dto import UserDTO
from module.user.user_model import UserModel


class UserAlteration:
    SessionLocal: sessionmaker[Session]

    def __init__(self):
        pass

    def created(self, user_dto: UserDTO) -> None:

        user_dto = user_dto.model_dump()
        model = UserModel(**user_dto)

        with self.SessionLocal() as session:
            session.add(model)
            session.commit()

            session.refresh(model)

            return model

    def updated(self, user_dto: UserDTO) -> None:

        if user_dto.id is None:
            return None

        with self.SessionLocal() as session:
            user = session.get(UserModel, user_dto.id)

            user.name = user_dto.name
            user.cpf = user_dto.cpf
            user.email = user_dto.email
            user.password = user_dto.password
            user.role = user_dto.role
            user.perfil = user_dto.perfil

            session.commit()
            session.refresh(user)

            return user

    def deleted(self, id: str) -> bool:

        with self.SessionLocal() as session:
            user = session.get(UserModel, id)

            if not user:
                return False

            session.delete(user)
            session.commit()

            return True
