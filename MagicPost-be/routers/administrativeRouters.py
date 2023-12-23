from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.administrative import AdministrativeRegionModel, AdministrativeUnitModel, ProvinceModel, DistrictModel, WardModel
from schemas.administrativeSchema import AdministrativeRegion, AdministrativeUnit, Province, District, Ward
from database import getDatabase
from typing import List

router = APIRouter(
    prefix="/api/v1/administrative",
    tags=["administrative"],
    responses={404: {"description": "Not found"}},
)

# API endpoint to get all administrative regions
@router.get("/administrative_regions/", response_model=List[AdministrativeRegion])
async def get_administrative_regions(skip: int = 0, limit: int = 10, db: Session = Depends(getDatabase)):
    regions = db.query(AdministrativeRegionModel).offset(skip).limit(limit).all()
    return regions

# API endpoint to get a specific administrative region by ID
@router.get("/administrative_regions/{region_id}", response_model=AdministrativeRegion)
async def get_administrative_region(region_id: int, db: Session = Depends(getDatabase)):
    region = db.query(AdministrativeRegionModel).filter(AdministrativeRegionModel.id == region_id).first()
    if region is None:
        raise HTTPException(status_code=404, detail="Region not found")
    return region

# API endpoint to get all administrative units
@router.get("/administrative_units/", response_model=List[AdministrativeUnit])
async def get_administrative_units(skip: int = 0, limit: int = 10, db: Session = Depends(getDatabase)):
    units = db.query(AdministrativeUnitModel).offset(skip).limit(limit).all()
    return units

# API endpoint to get a specific administrative unit by ID
@router.get("/administrative_units/{unit_id}", response_model=AdministrativeUnit)
async def get_administrative_unit(unit_id: int, db: Session = Depends(getDatabase)):
    unit = db.query(AdministrativeUnitModel).filter(AdministrativeUnitModel.id == unit_id).first()
    if unit is None:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit

# API endpoint to get all provinces
@router.get("/provinces/", response_model=List[Province])
async def get_provinces(skip: int = 0, limit: int = 10, db: Session = Depends(getDatabase)):
    provinces = db.query(ProvinceModel).offset(skip).limit(limit).all()
    return provinces

# API endpoint to get a specific province by ID
@router.get("/provinces/{province_id}", response_model=Province)
async def get_province(province_id: int, db: Session = Depends(getDatabase)):
    province = db.query(ProvinceModel).filter(ProvinceModel.code == province_id).first()
    if province is None:
        raise HTTPException(status_code=404, detail="Province not found")
    return province

# API endpoint to get all districts
@router.get("/districts/", response_model=List[District])
async def get_districts(skip: int = 0, limit: int = 10, db: Session = Depends(getDatabase)):
    districts = db.query(DistrictModel).offset(skip).limit(limit).all()
    return districts

# API endpoint to get a specific district by ID
@router.get("/districts/{district_id}", response_model=District)
async def get_district(district_id: int, db: Session = Depends(getDatabase)):
    district = db.query(DistrictModel).filter(DistrictModel.code == district_id).first()
    if district is None:
        raise HTTPException(status_code=404, detail="District not found")
    return district

# API endpoint to get all wards
@router.get("/wards/", response_model=List[Ward])
async def get_wards(skip: int = 0, limit: int = 10, db: Session = Depends(getDatabase)):
    wards = db.query(WardModel).offset(skip).limit(limit).all()
    return wards

# API endpoint to get a specific ward by ID
@router.get("/wards/{ward_id}", response_model=Ward)
async def get_ward(ward_id: int, db: Session = Depends(getDatabase)):
    ward = db.query(WardModel).filter(WardModel.code == ward_id).first()
    if ward is None:
        raise HTTPException(status_code=404, detail="Ward not found")
    return ward

# API endpoint to get all provinces in a specific administrative region
@router.get("/administrative_regions/{region_id}/provinces/", response_model=List[Province])
async def get_provinces_by_region(region_id: int, db: Session = Depends(getDatabase)):
    provinces = db.query(ProvinceModel).filter(ProvinceModel.administrative_region_id == region_id).all()
    if provinces is None:
        raise HTTPException(status_code=404, detail="Provinces not found")
    return provinces

# API endpoint to get all districts in a specific province
@router.get("/provinces/{province_id}/districts/", response_model=List[District])
async def get_districts_by_province(province_id: int, db: Session = Depends(getDatabase)):
    districts = db.query(DistrictModel).filter(DistrictModel.province_code == province_id).all()
    if districts is None:
        raise HTTPException(status_code=404, detail="Districts not found")
    return districts

# API endpoint to get all wards in a specific district
@router.get("/districts/{district_id}/wards/", response_model=List[Ward])
async def get_wards_by_district(district_id: int, db: Session = Depends(getDatabase)):
    wards = db.query(WardModel).filter(WardModel.district_code == district_id).all()
    if wards is None:
        raise HTTPException(status_code=404, detail="Wards not found")
    return wards

# API endpoint to get all districts in a specific administrative region
@router.get("/administrative_regions/{region_id}/districts/", response_model=List[District])
async def get_districts_by_region(region_id: int, db: Session = Depends(getDatabase)):
    districts = db.query(DistrictModel).join(ProvinceModel, ProvinceModel.code == DistrictModel.province_code).filter(ProvinceModel.administrative_region_id == region_id).all()
    if districts is None:
        raise HTTPException(status_code=404, detail="Districts not found")
    return districts
