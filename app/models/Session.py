from sqlalchemy import Integer, DateTime, Table, ForeignKey, JSON, Boolean, LargeBinary, String
from sqlalchemy.orm import relationship, mapped_column, DeclarativeBase

class Session(DeclarativeBase):
    __tablename__ = "__sessions"
    id = mapped_column(Integer(), primary_key=True)
    session_id = mapped_column(String(), unique=True)
    data = mapped_column(LargeBinary())
    expiry = mapped_column(DateTime())