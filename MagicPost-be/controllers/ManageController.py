from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.manage import (
    GatheringLeaderModel,
    GatheringStaffModel,
    TransactionLeaderModel,
    TransactionStaffModel,
    GatheringPointModel,
    TransactionPointModel,
)
from schemas.manageSchema import (
    GatheringLeader,
    GatheringStaff,
    TransactionLeader,
    TransactionStaff,
    GatheringPoint,
    TransactionPointCreate,
    GatheringPointCreate,
    Destination,
)
from schemas.userSchema import RegisterUser
from controllers.AuthController import AuthController


class ManageController:
    def getAllGatheringPoints(db: Session):
        return db.query(GatheringPointModel).all()

    def getAllGatheringLeaders(db: Session):
        return db.query(GatheringLeaderModel).all()

    def getAllGatheringStaffs(db: Session):
        return db.query(GatheringStaffModel).all()

    def getAllTransactionPoints(db: Session):
        return db.query(TransactionPointModel).all()

    def getAllTransactionPointsByDestination(destination: Destination, db: Session):
        is_transaction_point_exist_by_ward = (
            db.query(TransactionPointModel)
            .filter(
                TransactionPointModel.province_code == destination.province_code,
                TransactionPointModel.district_code == destination.district_code,
                TransactionPointModel.ward_code == destination.ward_code,
            )
            .first()
        )
        if not is_transaction_point_exist_by_ward:
            is_transaction_point_exist_by_district = (
                db.query(TransactionPointModel)
                .filter(
                    TransactionPointModel.province_code == destination.province_code,
                    TransactionPointModel.district_code == destination.district_code,
                )
                .first()
            )
            if not is_transaction_point_exist_by_district:
                return (
                    db.query(TransactionPointModel)
                    .filter(
                        TransactionPointModel.province_code
                        == destination.province_code,
                    )
                    .all()
                )
            return (
                db.query(TransactionPointModel)
                .filter(
                    TransactionPointModel.province_code == destination.province_code,
                    TransactionPointModel.district_code == destination.district_code,
                )
                .all()
            )
        return (
            db.query(TransactionPointModel)
            .filter(
                TransactionPointModel.province_code == destination.province_code,
            )
            .all()
        )

    def getAllTransactionLeaders(db: Session):
        return db.query(TransactionLeaderModel).all()

    def getAllTransactionStaffs(db: Session):
        return db.query(TransactionStaffModel).all()

    def createGatheringPoint(gathering_point: GatheringPointCreate, db: Session):
        new_gathering_point = GatheringPointModel(name=gathering_point.name)
        db.add(new_gathering_point)
        db.commit()
        db.refresh(new_gathering_point)
        return new_gathering_point

    def createTransactionPoint(transaction_point: TransactionPointCreate, db: Session):
        new_transaction_point = TransactionPointModel(
            name=transaction_point.name,
            province_code=transaction_point.province_code,
            district_code=transaction_point.district_code,
            ward_code=transaction_point.ward_code,
            address=transaction_point.address,
            phone=transaction_point.phone,
            gathering_point_id=transaction_point.gathering_point_id,
        )
        db.add(new_transaction_point)
        db.commit()
        db.refresh(new_transaction_point)
        return new_transaction_point

    def createGatheringLeader(
        register: RegisterUser, gathering_point_id: int, db: Session
    ):
        is_gathering_leader_exist = (
            db.query(GatheringLeaderModel)
            .filter(GatheringLeaderModel.gathering_point_id == gathering_point_id)
            .first()
        )
        if is_gathering_leader_exist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Gathering leader already exist",
            )
        new_user = AuthController.createUser(register, db)
        new_user_id = new_user["user"].id
        new_gathering_leader = GatheringLeaderModel(
            user_id=new_user_id,
            gathering_point_id=gathering_point_id,
        )
        db.add(new_gathering_leader)
        db.commit()
        db.refresh(new_gathering_leader)
        return {"user": new_user, "user_detail": new_gathering_leader}

    def createTransactionLeader(
        register: RegisterUser, transaction_point_id: int, db: Session
    ):
        is_transaction_leader_exist = (
            db.query(TransactionLeaderModel)
            .filter(TransactionLeaderModel.transaction_point_id == transaction_point_id)
            .first()
        )
        if is_transaction_leader_exist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Transaction leader already exist",
            )
        new_user = AuthController.createUser(register, db)
        new_user_id = new_user["user"].id
        new_transaction_leader = TransactionLeaderModel(
            user_id=new_user_id,
            transaction_point_id=transaction_point_id,
        )
        db.add(new_transaction_leader)
        db.commit()
        db.refresh(new_transaction_leader)
        return {"user": new_user, "user_detail": new_transaction_leader}

    def createGatheringStaff(
        register: RegisterUser, gathering_point_id: int, db: Session
    ):
        new_user = AuthController.createUser(register, db)
        new_user_id = new_user["user"].id
        new_gathering_staff = GatheringStaffModel(
            user_id=new_user_id,
            gathering_point_id=gathering_point_id,
        )
        db.add(new_gathering_staff)
        db.commit()
        db.refresh(new_gathering_staff)
        return {"user": new_user, "user_detail": new_gathering_staff}

    def createTransactionStaff(
        register: RegisterUser, transaction_point_id: int, db: Session
    ):
        new_user = AuthController.createUser(register, db)
        new_user_id = new_user["user"].id
        new_transaction_staff = TransactionStaffModel(
            user_id=new_user_id,
            transaction_point_id=transaction_point_id,
        )
        db.add(new_transaction_staff)
        db.commit()
        db.refresh(new_transaction_staff)
        return {"user": new_user, "user_detail": new_transaction_staff}
