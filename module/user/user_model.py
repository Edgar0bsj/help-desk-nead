from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from database.database_config import Base


class UserModel(Base):
    __tablename__ = "user"

    id: Mapped[str] = mapped_column(primary_key=True, unique=True)

    name: Mapped[str] = mapped_column(String(50), nullable=False)

    cpf: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)

    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    password: Mapped[str] = mapped_column(String(225), nullable=False)

    role: Mapped[str] = mapped_column(String(50), nullable=False)

    perfil: Mapped[str] = mapped_column(String(50), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )
