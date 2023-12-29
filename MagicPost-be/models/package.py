from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Enum, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import database
import enum

class PackageType(str, enum.Enum):
    DOCUMENT = "document"
    GOODS = "goods"
    
class PackageStatus(str, enum.Enum):
    WAITING = "waiting"
    STORING = "storing"
    DELIVERED = "delivered"
    SHIPPING = "shipping"
    CANCELED = "canceled"
    SUCCESS = "success"

class PackageModel(database.Base):
    __tablename__ = "package"

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    name = Column(String(255), index=True)
    price = Column(Integer)
    description = Column(String(255))
    image = Column(String(255))
    transaction_point_id = Column(Integer, ForeignKey("transaction_point.id"))
    destination_transaction_id = Column(Integer, ForeignKey("transaction_point.id"))
    gathering_point_id = Column(Integer, ForeignKey("gathering_point.id"))
    destination_gathering_id = Column(Integer, ForeignKey("gathering_point.id"))
    sender_name = Column(String(255))
    sender_phone = Column(String(255))
    sender_province_code = Column(Integer)
    sender_district_code = Column(Integer)
    sender_ward_code = Column(Integer)
    sender_address = Column(String(255))
    receiver_name = Column(String(255))
    receiver_phone = Column(String(255))
    receiver_province_code = Column(Integer)
    receiver_district_code = Column(Integer)
    receiver_ward_code = Column(Integer)
    receiver_address = Column(String(255))
    weight = Column(Float, default=0.0)
    type = Column(Enum(PackageType), default=PackageType.GOODS)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    
    package_status = relationship("PackageStatusModel", back_populates="package")
    context_order = relationship("ContextOrderModel", back_populates="package")
    
    
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
    
    package = relationship("PackageModel", back_populates="context_order")
    

class PackageStatusModel(database.Base):
    __tablename__ = "package_status"

    id = Column(BigInteger, primary_key=True, index=True)
    package_id = Column(BigInteger, ForeignKey("package.id"))
    status = Column(Enum(PackageStatus), default=PackageStatus.WAITING)
    fail_reason = Column(String(255), nullable=True)
    transaction_point_id = Column(Integer, ForeignKey("transaction_point.id"), nullable=True)
    gathering_point_id = Column(Integer, ForeignKey("gathering_point.id"), nullable=True)
    shipper_id = Column(Integer, ForeignKey("shipper.id"), nullable=True)
    received_time = Column(DateTime, nullable=True)
    delivered_time = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    
    package = relationship("PackageModel", back_populates="package_status")
    