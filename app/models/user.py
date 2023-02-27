from sqlalchemy import Integer, DateTime, Table, ForeignKey, JSON, Boolean, LargeBinary, String
from sqlalchemy.orm import relationship, mapped_column
from app.models import Base

class User(Base):
    __tablename__ = "user"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)

    # Independent columns
    name = mapped_column(String)
    username = mapped_column(String, default="")
    hpassword = mapped_column(String, default="") # hashed password
    login_attempts = mapped_column(Integer, default=0)
    last_login_time = mapped_column(DateTime)
    role = mapped_column(String, default="") 

    def dict(self):
        d = {
            "user_id": self.id,
            "name": self.name,
            "username": self.username,
            "role": self.role,
        }
        return d

    def update(self, data):
        for field in ["name", "username", "hpassword", "role"]:
            if value := data.get(field):
                setattr(self, field, value)