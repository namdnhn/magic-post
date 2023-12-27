from enum import Enum
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Roles(str, Enum):
    ADMIN = "admin"
    TRANSACTION_LEADER = "transaction_leader"
    TRANSACTION_STAFF = "transaction_staff"
    GATHERING_LEADER = "gathering_leader"
    GATHERS_STAFF = "gathering_staff"
    CUSTOMER = "customer"
    SHIPPER = "shipper"
    
class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class Login(BaseModel):
    email: str
    password: str
    
class RegisterUser(BaseModel):
    email: str
    password: str
    fullname: str
    date_of_birth: datetime
    gender: Gender = Gender.OTHER
    role: Roles = Roles.CUSTOMER
    phone: str
    image_path: str = ""
    address: str

    class Config:
        orm_mode = True
        
class ConfirmPassword(BaseModel):
    currentPass: str


class UpdateUser(ConfirmPassword):
    fullname: Optional[str] = None
    email: Optional[str] = None
    newPassword: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    gender: Optional[Gender] = None
    role: Optional[Roles] = None
    phone: Optional[str] = None
    image_path: Optional[str] = None
    address: Optional[str] = None