from sqlalchemy import Column, Integer, String, ForeignKey, Index
from sqlalchemy.orm import relationship
import database

class Admin(database.Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
class GatheringPointModel(database.Base):
    __tablename__ = "gathering_point"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    
    gathering_leader = relationship("GatheringLeaderModel", back_populates="gathering_point")
    gathering_staffs = relationship("GatheringStaffModel", back_populates="gathering_point")
    transaction_points = relationship("TransactionPointModel", back_populates="gathering_point")
    
class TransactionPointModel(database.Base):
    __tablename__ = "transaction_point"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    province_code = Column(String(50), ForeignKey("provinces.code"))
    district_code = Column(String(50), ForeignKey("districts.code"))
    ward_code = Column(String(50), ForeignKey("wards.code"))
    address = Column(String(255))
    phone = Column(String(255))
    gathering_point_id = Column(Integer, ForeignKey("gathering_point.id"))
    
    transaction_leader = relationship("TransactionLeaderModel", back_populates="transaction_point")
    transaction_staffs = relationship("TransactionStaffModel", back_populates="transaction_point")
    gathering_point = relationship("GatheringPointModel", back_populates="transaction_points")
    shippers = relationship("ShipperModel", back_populates="transaction_point")
    
class GatheringLeaderModel(database.Base):
    __tablename__ = "gathering_leader"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    gathering_point_id = Column(Integer, ForeignKey("gathering_point.id"))
    
    gathering_point = relationship("GatheringPointModel", back_populates="gathering_leader")
    
class GatheringStaffModel(database.Base):
    __tablename__ = "gathering_staff"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    gathering_point_id = Column(Integer, ForeignKey("gathering_point.id"))
    
    gathering_point = relationship("GatheringPointModel", back_populates="gathering_staffs")
    
class TransactionLeaderModel(database.Base):
    __tablename__ = "transaction_leader"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    transaction_point_id = Column(Integer, ForeignKey("transaction_point.id"))
    
    transaction_point = relationship("TransactionPointModel", back_populates="transaction_leader")
    
class TransactionStaffModel(database.Base):
    __tablename__ = "transaction_staff"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    transaction_point_id = Column(Integer, ForeignKey("transaction_point.id"))
    
    transaction_point = relationship("TransactionPointModel", back_populates="transaction_staffs")
    
class ShipperModel(database.Base):
    __tablename__ = "shipper"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    transaction_point_id = Column(Integer, ForeignKey("transaction_point.id"))
    
    transaction_point = relationship("TransactionPointModel", back_populates="shippers")