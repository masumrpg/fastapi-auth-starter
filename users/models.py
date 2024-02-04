import uuid
from sqlalchemy import Boolean, Column, String, DateTime, func
from datetime import datetime
from core.database import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, nullable=False, default=str(uuid.uuid4()))
    username = Column(String, unique=True,nullable=False, index=True)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    full_name = Column(String(200), nullable=False,)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    verified_at = Column(DateTime, nullable=True, default=None)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())