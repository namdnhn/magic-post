from pydantic import BaseModel
from typing import Optional, List
from schemas.packageSchema import Package

class AdminBase(BaseModel):
    user_id: int

class AdminCreate(AdminBase):
    pass

class Admin(AdminBase):
    id: int

    class Config:
        orm_mode = True


class GatheringPointBase(BaseModel):
    name: str
    address: Optional[str] = None
    phone: Optional[str] = None

class GatheringPointCreate(GatheringPointBase):
    pass

class GatheringPointCreateByCurrentUser(GatheringPointBase):
    user_email: str


class TransactionPointBase(BaseModel):
    name: str
    province_code: int
    district_code: int
    ward_code: int
    address: str
    phone: str
    gathering_point_id: int

class TransactionPointCreate(TransactionPointBase):
    pass

class TransactionPointCreateByCurrentUser(TransactionPointBase):
    user_email: str

class TransactionPoint(TransactionPointBase):
    id: int
    
    packages: Optional[List[Package]] = None

    class Config:
        orm_mode = True


class GatheringLeaderBase(BaseModel):
    user_id: int
    gathering_point_id: int

class GatheringLeaderCreate(GatheringLeaderBase):
    pass

class GatheringLeader(GatheringLeaderBase):
    id: int

    class Config:
        orm_mode = True


class GatheringStaffBase(BaseModel):
    user_id: int
    gathering_point_id: int

class GatheringStaffCreate(GatheringStaffBase):
    pass

class GatheringStaff(GatheringStaffBase):
    id: int

    class Config:
        orm_mode = True


class TransactionLeaderBase(BaseModel):
    user_id: int
    transaction_point_id: int

class TransactionLeaderCreate(TransactionLeaderBase):
    pass

class TransactionLeader(TransactionLeaderBase):
    id: int

    class Config:
        orm_mode = True


class TransactionStaffBase(BaseModel):
    user_id: int
    transaction_point_id: int

class TransactionStaffCreate(TransactionStaffBase):
    pass

class TransactionStaff(TransactionStaffBase):
    id: int

    class Config:
        orm_mode = True


class ShipperBase(BaseModel):
    user_id: int
    transaction_point_id: int

class ShipperCreate(ShipperBase):
    pass

class Shipper(ShipperBase):
    id: int

    class Config:
        orm_mode = True
        
class Destination(BaseModel):
    province_code: int
    district_code: int
    ward_code: int

class Roles(BaseModel):
    id: str
    name: str

class WorkAt(BaseModel):
    id: str
    pointId: str
    name: str

class Staff(BaseModel):
    id: str
    userId: str
    address: str
    email: str
    fullName: str
    phoneNo: str
    dateOfBirth: str
    role: Roles
    workAt: WorkAt

class GatheringPoint(BaseModel):
    id: str
    pointId: str
    name: str
    
class Leader(BaseModel):
    userId: str
    fullName: str
    
class Offices(BaseModel):
    id: str
    pointId: str
    name: str
    phoneNo: Optional[str] = None
    address: Optional[str] = None
    leader: Leader
    gatheringPoint: Optional[GatheringPoint] = None
    type: str
