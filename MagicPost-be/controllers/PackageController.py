from fastapi import HTTPException, status, Depends
from database import getDatabase

from sqlalchemy.orm import Session
from models.package import (
    PackageModel,
    ContextOrderModel,
    PackageStatusModel,
)
from schemas.packageSchema import (
    PackageCreate,
    Package,
    ContextOrderCreate,
    ContextOrder,
    PackageStatusCreate,
    PackageStatus,
    FullPackage
)


class PackageController:
    def getAllPackage(db: Session):
        return db.query(PackageModel).all()
    
    def getPackage(package_id: int, db: Session):
        package = db.query(PackageModel).filter(PackageModel.id == package_id).first()
        if not package:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Package not found",
            )
        return package
    
    def createPackage(package: PackageCreate, contextCreate: ContextOrderCreate = None, db: Session = Depends(getDatabase)):
        package = PackageModel(**package.model_dump())
        db.add(package)
        db.commit()
        db.refresh(package)
        if contextCreate:
            contextCreate.package_id = package.id
            contextCreate = ContextOrderModel(**contextCreate.model_dump())
            db.add(contextCreate)
            db.commit()
            db.refresh(contextCreate)
        package_status = PackageStatusModel(package_id=package.id, status="Đã tiếp nhận", transaction_point_id=package.transaction_point_id)
        db.add(package_status)
        db.commit()
        db.refresh(package_status)
        return FullPackage(package=package, context_order=contextCreate, package_status=package_status)
    
    def updatePackageStatus(package_id: int, package_status: PackageStatusCreate, db: Session):
        package = db.query(PackageModel).filter(PackageModel.id == package_id).first()
        if not package:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Package not found",
            )
        package_status = PackageStatusModel(**package_status.model_dump())
        db.add(package_status)
        db.commit()
        db.refresh(package_status)
        return package_status
    
    def getAllContextOrder(package_id: int, db: Session):
        package = db.query(PackageModel).filter(PackageModel.id == package_id).first()
        if not package:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Package not found",
            )
        return package.context_order
    
    def getAllPackageStatus(package_id: int, db: Session):
        package = db.query(PackageModel).filter(PackageModel.id == package_id).first()
        if not package:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Package not found",
            )
        return package.package_status
    