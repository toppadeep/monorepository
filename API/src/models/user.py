from sqlalchemy import Integer, String, Column
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    website = Column(String)
    company_name = Column(String, name="company_name")
