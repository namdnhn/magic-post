from typing import List, Optional
from pydantic import BaseModel, HttpUrl
from enum import Enum

class PackageType(str, Enum):
    DOCUMENT = "document"
    GOODS = "goods"

class PackageBase(BaseModel):
    name: str
    price: int
    description: str
    image: str
    transaction_point_id: int
    destination_id: int
    sender_name: str
    sender_phone: str
    sender_province_code: int
    sender_district_code: int
    sender_ward_code: int
    sender_address: str
    receiver_name: str
    receiver_phone: str
    receiver_province_code: int
    receiver_district_code: int
    receiver_ward_code: int
    receiver_address: str
    weight: float = 0.0
    package_type: PackageType = PackageType.GOODS

class PackageCreate(PackageBase):
    pass

class Package(PackageBase):
    id: int
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True

class ContextOrderBase(BaseModel):
    package_id: int
    context: str
    quantity: int
    value: int

class ContextOrderCreate(ContextOrderBase):
    pass

class ContextOrder(ContextOrderBase):
    id: int
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True

class PackageStatusBase(BaseModel):
    package_id: int
    status: str
    fail_reason: str = None
    transaction_point_id: int = None
    gathering_point_id: int = None
    shipper_id: int = None

class PackageStatusCreate(PackageStatusBase):
    pass

class PackageStatus(PackageStatusBase):
    id: int
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True
        
class FullPackage(BaseModel):
    package: Package
    context_order: Optional[List[ContextOrder]] = None
    package_status: List[PackageStatus]
    