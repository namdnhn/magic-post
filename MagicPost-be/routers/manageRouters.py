from fastapi import APIRouter, HTTPException, Depends
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import getDatabase
from controllers.ManageController import ManageController
from schemas.manageSchema import (
    GatheringPointCreate,
    TransactionPointCreate,
    Destination,
    GatheringPoint,
    GatheringLeader,
    GatheringStaff,
    TransactionPoint,
    TransactionLeader,
    TransactionStaff
)
from schemas.userSchema import RegisterUser
from typing import List

router = APIRouter(
    prefix="/api/v1/manage",
    tags=["manage"],
    responses={404: {"description": "Not found"}},
)

@router.get("/gathering_points/", response_model=List[GatheringPoint])
async def get_all_gathering_points(db: Session = Depends(getDatabase)):
    return ManageController.getAllGatheringPoints(db)

@router.get("/gathering_leaders/", response_model=List[GatheringLeader])
async def get_all_gathering_leaders(db: Session = Depends(getDatabase)):
    return ManageController.getAllGatheringLeaders(db)

@router.get("/gathering_staffs/", response_model=List[GatheringStaff])
async def get_all_gathering_staffs(db: Session = Depends(getDatabase)):
    return ManageController.getAllGatheringStaffs(db)

@router.get("/transaction_points/", response_model=List[TransactionPoint])
async def get_all_transaction_points(db: Session = Depends(getDatabase)):
    return ManageController.getAllTransactionPoints(db)

@router.get("/transaction_points_by_destination/", response_model=List[TransactionPoint])
async def get_all_transaction_points_by_destination(destination: Destination, db: Session = Depends(getDatabase)):
    return ManageController.getAllTransactionPointsByDestination(destination, db)

@router.get("/transaction_leaders/", response_model=List[TransactionLeader])
async def get_all_transaction_leaders(db: Session = Depends(getDatabase)):
    return ManageController.getAllTransactionLeaders(db)

@router.get("/transaction_staffs/", response_model=List[TransactionStaff])
async def get_all_transaction_staffs(db: Session = Depends(getDatabase)):
    return ManageController.getAllTransactionStaffs(db)

@router.post("/gathering_point/")
async def create_gathering_point(gathering_point: GatheringPointCreate, db: Session = Depends(getDatabase)):
    return ManageController.createGatheringPoint(gathering_point, db)

@router.post("/transaction_point/")
async def create_transaction_point(transaction_point: TransactionPointCreate, db: Session = Depends(getDatabase)):
    return ManageController.createTransactionPoint(transaction_point, db)

@router.post("/gathering_leader/{gathering_point_id}")
async def create_gathering_leader(register_user: RegisterUser, gathering_point_id: int, db: Session = Depends(getDatabase)):
    return ManageController.createGatheringLeader(register_user, gathering_point_id, db)

@router.post("/gathering_staff/{gathering_point_id}")
async def create_gathering_staff(register_user: RegisterUser, gathering_point_id: int, db: Session = Depends(getDatabase)):
    return ManageController.createGatheringStaff(register_user, gathering_point_id, db)

@router.post("/transaction_leader/{transaction_point_id}")
async def create_transaction_leader(register_user: RegisterUser, transaction_point_id: int, db: Session = Depends(getDatabase)):
    return ManageController.createTransactionLeader(register_user, transaction_point_id, db)

@router.post("/transaction_staff/{transaction_point_id}")
async def create_transaction_staff(register_user: RegisterUser, transaction_point_id: int, db: Session = Depends(getDatabase)):
    return ManageController.createTransactionStaff(register_user, transaction_point_id, db)
