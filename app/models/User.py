from sqlalchemy import Integer, DateTime, Table, ForeignKey, JSON, Boolean, LargeBinary, String
from sqlalchemy.orm import relationship, mapped_column, DeclarativeBase

class User(DeclarativeBase):
    __tablename__ = "user"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)

    # Independent columns
    name = mapped_column(String)
    username = mapped_column(String, default="")
    password_hash = mapped_column(String, default="")
    login_attempts = mapped_column(Integer, default=0)
    last_login_time = mapped_column(DateTime)
    role = mapped_column(String, default="student")  # student, parent, teacher

    def to_client(self):
        d = {
            "user_id": self.id,
            "name": self.name,
            "username": self.username,
            "password_hash": self.password_hash,
            "role": self.role,
            "exams": []
        }
        for exam in self.exams:
            d["exams"].append({"id": exam.id, "name": exam.name})
        return d

    def update(self, data):
        for field in ["name", "username", "password_hash", "role"]:
            if value := data.get(field):
                setattr(self, field, value)