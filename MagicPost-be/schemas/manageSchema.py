from pydantic import BaseModel
from typing import Optional

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

class GatheringPointCreate(GatheringPointBase):
    pass

class GatheringPoint(GatheringPointBase):
    id: int

    class Config:
        orm_mode = True


class TransactionPointBase(BaseModel):
    name: str
    province_code: str
    district_code: str
    ward_code: str
    address: str
    phone: str
    gathering_point_id: int

class TransactionPointCreate(TransactionPointBase):
    pass

class TransactionPoint(TransactionPointBase):
    id: int

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
    province_code: str
    district_code: str
    ward_code: str