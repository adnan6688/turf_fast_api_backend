from sqlalchemy import Column,Integer,String,DateTime,Enum
from sqlalchemy.sql import func

from database import Base
import enum 



class UserRole(str,enum.Enum):
        USER='USER'
        STAFF='STAFF'
        ADMIN='ADMIN'


class User(Base):
    __tablename__ = "User"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50) , nullable=False)
    email = Column(String(50) , unique=True,index=True,nullable=False)
    password = Column(String,nullable=False)
    phone = Column(String(20) , nullable=False)
    role = Column(Enum(UserRole) , default=UserRole.USER)

    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(DateTime(timezone=True) , onupdate=func.now())