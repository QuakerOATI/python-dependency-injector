from sqlalchemy import Column, String, Boolean, Integer
from textwrap import dedent

from .database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return dedent(f"""
            <User(id={self.id},
                email="{self.email}",
                hashed_password="{self.hashed_password}",
                is_active={self.is_active})>
        """)
