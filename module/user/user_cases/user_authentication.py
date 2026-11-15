from datetime import UTC, datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session, sessionmaker

from module.user.user_dto import UserDTO


class UserAuthentication:
    SessionLocal: sessionmaker[Session]

    def __init__(self):
        self.SECRET_KEY = "ping_pong"
        self.ALGORITHM = "HS256"
        self.ACCESS_TOKEN_EXPIRE_MINUTES = 60

        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def make_password_hash(self, password: str) -> str:
        return str(self.pwd_context.hash(password))

    def password_validation(self, password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(password, hashed_password)

    def make_token_generation(self, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(UTC) + expires_delta
        else:
            expire = datetime.now(UTC) + timedelta(minutes=15)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    def response_to_the_user(self):
        pass
