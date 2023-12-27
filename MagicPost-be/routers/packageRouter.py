from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import getDatabase
from controllers.PackageController import PackageController
from schemas.packageSchema import (
    PackageCreate,
    Package,
    ContextOrderCreate,
    ContextOrder,
    PackageStatusCreate,
    PackageStatus,
)
from typing import List

router = APIRouter(
    prefix="/api/v1/package",
    tags=["package"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[Package])
def getAllPackage(db: Session = Depends(getDatabase)):
    return PackageController.getAllPackage(db)

@router.get("/{package_id}", response_model=Package)
def getPackage(package_id: int, db: Session = Depends(getDatabase)):
    return PackageController.getPackage(package_id, db)

@router.get("/{package_id}/context_order", response_model=List[ContextOrder])
def getAllContextOrder(package_id: int, db: Session = Depends(getDatabase)):
    return PackageController.getAllContextOrder(package_id, db)

@router.get("/{package_id}/package_status", response_model=List[PackageStatus])
def getAllPackageStatus(package_id: int, db: Session = Depends(getDatabase)):
    return PackageController.getAllPackageStatus(package_id, db)

@router.post("/", response_model=Package)
def createPackage(package: PackageCreate, context: ContextOrderCreate = None, db: Session = Depends(getDatabase)):
    return PackageController.createPackage(package, context, db)

@router.post("/{package_id}/status", response_model=PackageStatus)
def updatePackageStatus(package_id: int, package_status: PackageStatusCreate, db: Session = Depends(getDatabase)):
    return PackageController.updatePackageStatus(package_id, package_status, db)

