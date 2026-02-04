from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from database.database import Base

class PersonOrm(Base):
    __tablename__ = "person"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25), unique=True)
    hashpassword: Mapped[str] = mapped_column(String(72))
    email: Mapped[Optional[str]] =  mapped_column(String(50), unique=True, nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String(15), unique=True, nullable=True)