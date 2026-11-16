from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from database.database_config import Base


class TickerModel(Base):
    __tablename__ = "ticket"

    id: Mapped[str] = mapped_column(primary_key=True, unique=True)

    produto: Mapped[str] = mapped_column(String(50), nullable=False)

    titulo: Mapped[str] = mapped_column(String(225), nullable=False)

    descricao: Mapped[str] = mapped_column(String(400), nullable=False)

    fk_user_id: Mapped[str] = mapped_column(String(50), nullable=False)

    status: Mapped[str] = mapped_column(String(50), nullable=False)

    numero: Mapped[str] = mapped_column(String(25), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )
