from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Enum, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import database
import enum

class PackageType(str, enum.Enum):
    DOCUMENT = "document"
    GOODS = "goods"

class PackageModel(database.Base):
    __tablename__ = "package"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(255), index=True)
    price = Column(Integer)
    description = Column(String(255))
    image = Column(String(255))
    transaction_point_id = Column(Integer, ForeignKey("transaction_point.id"))
    destination_id = Column(Integer, ForeignKey("transaction_point.id"))
    sender_name = Column(String(255))
    sender_phone = Column(String(255))
    sender_province_code = Column(String(50), ForeignKey("provinces.code"))
    sender_district_code = Column(String(50), ForeignKey("districts.code"))
    sender_ward_code = Column(String(50), ForeignKey("wards.code"))
    sender_address = Column(String(255))
    receiver_name = Column(String(255))
    receiver_phone = Column(String(255))
    receiver_province_code = Column(String(50), ForeignKey("provinces.code"))
    receiver_district_code = Column(String(50), ForeignKey("districts.code"))
    receiver_ward_code = Column(String(50), ForeignKey("wards.code"))
    receiver_address = Column(String(255))
    weight = Column(Float, default=0.0)
    price = Column(Integer)
    type = Column(Enum(PackageType), default=PackageType.GOODS)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    
    
class ContextOrderModel(database.Base):
    __tablename__ = "context_order"
    
    id = Column(BigInteger, primary_key=True, index=True)
    package_id = Column(BigInteger, ForeignKey("package.id"))
    context = Column(String(255))
    quantity = Column(Integer)
    value = Column(Integer)
    document_type = Column(String(255))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    

class PackageStatusModel(database.Base):
    __tablename__ = "package_status"

    id = Column(BigInteger, primary_key=True, index=True)
    package_id = Column(BigInteger, ForeignKey("package.id"))
    status = Column(String(255))
    fail_reason = Column(String(255), nullable=True)
    transaction_point_id = Column(Integer, ForeignKey("transaction_point.id"), nullable=True)
    gathering_point_id = Column(Integer, ForeignKey("gathering_point.id"), nullable=True)
    shipper_id = Column(Integer, ForeignKey("shipper.id"), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    