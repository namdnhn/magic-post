import enum
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Enum
import database
from sqlalchemy.sql import func

class Roles(str, enum.Enum):
    ADMIN = "admin"
    TRANSACTION_LEADER = "transaction_leader"
    TRANSACTION_STAFF = "transaction_staff"
    GATHERING_LEADER = "gathering_leader"
    GATHERS_STAFF = "gathering_staff"
    CUSTOMER = "customer"
    SHIPPER = "shipper"
    
class Gender(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class UserModel(database.Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True)
    is_active = Column(Boolean, default=True)
    role = Column(Enum(Roles), default=Roles.CUSTOMER)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    
class UserDetailModel(database.Base):
    __tablename__ = "user_details"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    gender = Column(Enum(Gender), default=Gender.OTHER)
    date_of_birth = Column(DateTime, default=func.now())
    fullname = Column(String(255))
    phone = Column(String(255))
    address = Column(String(255))
    image_path = Column(String(255))
    

    
    
    
    