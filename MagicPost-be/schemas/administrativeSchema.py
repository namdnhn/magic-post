from typing import Optional
from pydantic import BaseModel

class AdministrativeRegionBase(BaseModel):
    name: str
    name_en: str
    code_name: Optional[str] = None
    code_name_en: Optional[str] = None

class AdministrativeRegionCreate(AdministrativeRegionBase):
    pass

class AdministrativeRegion(AdministrativeRegionBase):
    id: int
    class config:
        orm_mode = True

class AdministrativeUnitBase(BaseModel):
    full_name: Optional[str] = None
    full_name_en: Optional[str] = None
    short_name: Optional[str] = None
    short_name_en: Optional[str] = None
    code_name: Optional[str] = None
    code_name_en: Optional[str] = None

class AdministrativeUnitCreate(AdministrativeUnitBase):
    pass

class AdministrativeUnit(AdministrativeUnitBase):
    id: int
    class config:
        orm_mode = True

class ProvinceBase(BaseModel):
    code: str
    name: str
    name_en: Optional[str] = None
    full_name: str
    full_name_en: Optional[str] = None
    code_name: Optional[str] = None
    administrative_unit_id: Optional[int] = None
    administrative_region_id: Optional[int] = None

class ProvinceCreate(ProvinceBase):
    pass

class Province(ProvinceBase):
    code: int
    class config:
        orm_mode = True

class DistrictBase(BaseModel):
    code: str
    name: str
    name_en: Optional[str] = None
    full_name: Optional[str] = None
    full_name_en: Optional[str] = None
    code_name: Optional[str] = None
    province_code: Optional[str] = None
    administrative_unit_id: Optional[int] = None

class DistrictCreate(DistrictBase):
    pass

class District(DistrictBase):
    code: int
    class config:
        orm_mode = True

class WardBase(BaseModel):
    code: str
    name: str
    name_en: Optional[str] = None
    full_name: Optional[str] = None
    full_name_en: Optional[str] = None
    code_name: Optional[str] = None
    district_code: Optional[str] = None
    administrative_unit_id: Optional[int] = None

class WardCreate(WardBase):
    pass

class Ward(WardBase):
    code: int
    class config:
        orm_mode = True