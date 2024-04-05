from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Prompt(Base):
    __tablename__ = "prompt"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(256))
    text: Mapped[str] = mapped_column(String(4096))

    def __repr__(self) -> str:
        return f"Prompt(id={self.id!r}, title={self.title!r}, text={self.text!r})"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "text": self.text,
        }
