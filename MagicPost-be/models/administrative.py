from sqlalchemy import Column, Integer, String, ForeignKey, Index
from sqlalchemy.orm import relationship
import database

class AdministrativeRegionModel(database.Base):
    __tablename__ = "administrative_regions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    name_en = Column(String(50))
    code_name = Column(String(50), nullable=True)
    code_name_en = Column(String(50), nullable=True)

class AdministrativeUnitModel(database.Base):
    __tablename__ = "administrative_units"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(50), nullable=True)
    full_name_en = Column(String(50), nullable=True)
    short_name = Column(String(50), nullable=True)
    short_name_en = Column(String(50), nullable=True)
    code_name = Column(String(50), nullable=True)
    code_name_en = Column(String(50), nullable=True)

class ProvinceModel(database.Base):
    __tablename__ = "provinces"

    code = Column(String(50), primary_key=True, index=True)
    name = Column(String(50), index=True)
    name_en = Column(String(50), nullable=True)
    full_name = Column(String(50), index=True)
    full_name_en = Column(String(50), nullable=True)
    code_name = Column(String(50), nullable=True)
    administrative_unit_id = Column(Integer, ForeignKey("administrative_units.id"))
    administrative_region_id = Column(Integer, ForeignKey("administrative_regions.id"))

class DistrictModel(database.Base):
    __tablename__ = "districts"

    code = Column(String(50), primary_key=True, index=True)
    name = Column(String(50), index=True)
    name_en = Column(String(50), nullable=True)
    full_name = Column(String(50), nullable=True)
    full_name_en = Column(String(50), nullable=True)
    code_name = Column(String(50), nullable=True)
    province_code = Column(String(50), ForeignKey("provinces.code"))
    administrative_unit_id = Column(Integer, ForeignKey("administrative_units.id"))

class WardModel(database.Base):
    __tablename__ = "wards"

    code = Column(String(50), primary_key=True, index=True)
    name = Column(String(50), index=True)
    name_en = Column(String(50), nullable=True)
    full_name = Column(String(50), nullable=True)
    full_name_en = Column(String(50), nullable=True)
    code_name = Column(String(50), nullable=True)
    district_code = Column(String(50), ForeignKey("districts.code"))
    administrative_unit_id = Column(Integer, ForeignKey("administrative_units.id"))