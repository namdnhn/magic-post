from sqlalchemy import Column, Integer, String, ForeignKey
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
    address = Column(String(255))
    phone = Column(String(255))
    
    gathering_staffs = relationship("GatheringStaffModel", back_populates="gathering_point")
    gathering_leader = relationship("GatheringLeaderModel", back_populates="gathering_point")
    transaction_points = relationship("TransactionPointModel", back_populates="gathering_point")
    
class TransactionPointModel(database.Base):
    __tablename__ = "transaction_point"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    province_code = Column(Integer)
    district_code = Column(Integer)
    ward_code = Column(Integer)
    address = Column(String(255))
    phone = Column(String(255))
    gathering_point_id = Column(Integer, ForeignKey("gathering_point.id"))
    
    transaction_staffs = relationship("TransactionStaffModel", back_populates="transaction_point")
    transaction_leader = relationship("TransactionLeaderModel", back_populates="transaction_point")
    shippers = relationship("ShipperModel", back_populates="transaction_point")
    gathering_point = relationship("GatheringPointModel", back_populates="transaction_points")
    
class GatheringLeaderModel(database.Base):
    __tablename__ = "gathering_leader"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    gathering_point_id = Column(Integer, ForeignKey("gathering_point.id"))
    
    user = relationship("UserModel", back_populates="gathering_leader")
    gathering_point = relationship("GatheringPointModel", back_populates="gathering_leader")
    
class GatheringStaffModel(database.Base):
    __tablename__ = "gathering_staff"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    gathering_point_id = Column(Integer, ForeignKey("gathering_point.id"))
    
    user = relationship("UserModel", back_populates="gathering_staff")
    gathering_point = relationship("GatheringPointModel", back_populates="gathering_staffs")
    
class TransactionLeaderModel(database.Base):
    __tablename__ = "transaction_leader"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    transaction_point_id = Column(Integer, ForeignKey("transaction_point.id"))
    
    user = relationship("UserModel", back_populates="transaction_leader")
    transaction_point = relationship("TransactionPointModel", back_populates="transaction_leader")
    
class TransactionStaffModel(database.Base):
    __tablename__ = "transaction_staff"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    transaction_point_id = Column(Integer, ForeignKey("transaction_point.id"))
    
    user = relationship("UserModel", back_populates="transaction_staff")
    transaction_point = relationship("TransactionPointModel", back_populates="transaction_staffs")
    
    
class ShipperModel(database.Base):
    __tablename__ = "shipper"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    transaction_point_id = Column(Integer, ForeignKey("transaction_point.id"))
    
    user = relationship("UserModel", back_populates="shipper")
    transaction_point = relationship("TransactionPointModel", back_populates="shippers")