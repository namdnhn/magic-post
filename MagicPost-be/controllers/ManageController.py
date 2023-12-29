from typing import List
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
from models.user import Roles as UserRoles
from schemas.manageSchema import (
    GatheringLeader,
    GatheringStaff,
    TransactionLeader,
    TransactionStaff,
    GatheringPoint,
    GatheringPointCreateByCurrentUser,
    TransactionPointCreateByCurrentUser,
    TransactionPointCreate,
    GatheringPointCreate,
    Destination,
    Staff,
    Roles,
    WorkAt,
    Offices,
    Leader
)
from schemas.userSchema import RegisterUser
from controllers.AuthController import AuthController


class ManageController:
    def getAllGatheringPoints(db: Session):
        offices: List[Offices] = []
        gathering_points = db.query(GatheringPointModel).all()
        
        for point in gathering_points:
            leader = point.gathering_leader[0]
            fullname = AuthController.getFullnameByUserId(leader.user_id, db)
            new_office = Offices(
                id=str(point.id),
                pointId=str(point.id),
                name=point.name,
                phoneNo=point.phone,
                address=point.address,
                leader=Leader(
                    userId=str(leader.user_id),
                    fullName=fullname,
                ),
                type="Điểm tập kết",
            )
            offices.append(new_office)
            
        return offices

    def getGatheringPointByTransactionPoint(transaction_point_id: int, db: Session):
        transaction_point = (
            db.query(TransactionPointModel)
            .filter(TransactionPointModel.id == transaction_point_id)
            .first()
        )
        if not transaction_point:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Transaction point not found",
            )
        gathering_point = (
            db.query(GatheringPointModel)
            .filter(GatheringPointModel.id == transaction_point.gathering_point_id)
            .first()
        )
        if not gathering_point:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Gathering point not found",
            )
        return gathering_point
    
    def getAllGatheringPointsWithNoLeader(db: Session):
        offices: List[Offices] = []
        gathering_points = db.query(GatheringPointModel).all()
        
        for point in gathering_points:
            leader = point.gathering_leader[0]
            if not leader:
                new_office = Offices(
                    id=str(point.id),
                    pointId=str(point.id),
                    name=point.name,
                    phoneNo=point.phone,
                    address=point.address,
                    leader=Leader(
                        userId="",
                        fullName="",
                    ),
                    type="Điểm tập kết",
                )
                offices.append(new_office)
            
        return offices

    def getAllGatheringLeaders(db: Session):
        leaders: List[Staff] = []
        gathering_leaders = db.query(GatheringLeaderModel).all()
        
        for leader in gathering_leaders:
            user = leader.user
            user_detail = leader.user.user_detail[0]
            gathering_point = leader.gathering_point
            new_leader = Staff(
                id=str(leader.id),
                userId=str(leader.user_id),
                address=user_detail.address,
                email=user.email,
                fullName=user_detail.fullname,
                phoneNo=user_detail.phone,
                dateOfBirth=str(user_detail.date_of_birth),
                role=Roles(id=user.role, name=user.role),
                workAt=WorkAt(
                    id=str(leader.gathering_point_id),
                    pointId=str(leader.gathering_point_id),
                    name=gathering_point.name,
                ),
            )
            leaders.append(new_leader)
        return leaders

    def getAllGatheringStaffs(db: Session):
        staffs: List[Staff] = []
        gathering_staffs = db.query(GatheringStaffModel).all()

        for staff in gathering_staffs:
            user = staff.user
            user_detail = staff.user.user_detail[0]
            gathering_point = staff.gathering_point
            new_staff = Staff(
                id=str(staff.id),
                userId=str(staff.user_id),
                address=user_detail.address,
                email=user.email,
                fullName=user_detail.fullname,
                phoneNo=user_detail.phone,
                dateOfBirth=str(user_detail.date_of_birth),
                role=Roles(id=user.role, name=user.role),
                workAt=WorkAt(
                    id=str(staff.gathering_point_id),
                    pointId=str(staff.gathering_point_id),
                    name=gathering_point.name,
                ),
            )
            staffs.append(new_staff)
        return staffs

    def getAllTransactionPoints(db: Session):
        offices : List[Offices] = []
        transaction_points = db.query(TransactionPointModel).all()
        
        for point in transaction_points:
            leader = point.transaction_leader[0]
            fullname = AuthController.getFullnameByUserId(leader.user_id, db)
            new_office = Offices(
                id=str(point.id),
                pointId=str(point.id),
                name=point.name,
                phoneNo=point.phone,
                address=point.address,
                leader=Leader(
                    userId=str(leader.user_id),
                    fullName=fullname,
                ),
                type="Điểm giao dịch",
            )
            offices.append(new_office)
            
        return offices

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
                TransactionPointModel.district_code == destination.district_code,
                TransactionPointModel.ward_code == destination.ward_code,
            )
            .all()
        )

    def getAllTransactionLeaders(db: Session):
        leaders : List[Staff] = []
        transaction_leaders = db.query(TransactionLeaderModel).all()
        
        for leader in transaction_leaders:
            user = leader.user
            user_detail = leader.user.user_detail[0]
            transaction_point = leader.transaction_point
            new_leader = Staff(
                id=str(leader.id),
                userId=str(leader.user_id),
                address=user_detail.address,
                email=user.email,
                fullName=user_detail.fullname,
                phoneNo=user_detail.phone,
                dateOfBirth=str(user_detail.date_of_birth),
                role=Roles(id=user.role, name=user.role),
                workAt=WorkAt(
                    id=str(leader.transaction_point_id),
                    pointId=str(leader.transaction_point_id),
                    name=transaction_point.name,
                ),
            )
            leaders.append(new_leader)
            
        return leaders

    def getAllTransactionStaffs(db: Session):
        staffs: List[Staff] = []
        transaction_staffs = db.query(TransactionStaffModel).all()

        for staff in transaction_staffs:
            user = staff.user
            user_detail = staff.user.user_detail[0]
            transaction_point = staff.transaction_point
            new_staff = Staff(
                id=str(staff.id),
                userId=str(staff.user_id),
                address=user_detail.address,
                email=user.email,
                fullName=user_detail.fullname,
                phoneNo=user_detail.phone,
                dateOfBirth=str(user_detail.date_of_birth),
                role=Roles(id=user.role, name=user.role),
                workAt=WorkAt(
                    id=str(staff.transaction_point_id),
                    pointId=str(staff.transaction_point_id),
                    name=transaction_point.name,
                ),
            )
            staffs.append(new_staff)
        return staffs

    def getAllStaffs(db: Session):
        gathering_staffs = ManageController.getAllGatheringStaffs(db)
        transaction_staffs = ManageController.getAllTransactionStaffs(db)
        return gathering_staffs + transaction_staffs
    
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
    
    def createGatheringLeaderByCurrentUser(gathering_point_id: int, user_email: str, db: Session):
        user_id = AuthController.getUserIdByEmail(user_email, db)
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User not found",
            )
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
        new_gathering_leader = GatheringLeaderModel(
            user_id=user_id,
            gathering_point_id=gathering_point_id,
        )
        return new_gathering_leader
    
    def createTransactionLeaderByCurrentUser(transaction_point_id: int, user_email: str, db: Session):
        user_id = AuthController.getUserIdByEmail(user_email, db)
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User not found",
            )
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
        new_transaction_leader = TransactionLeaderModel(
            user_id=user_id,
            transaction_point_id=transaction_point_id,
        )
        return new_transaction_leader
    
    def createGatheringPointByCurrentUser(gathering_point: GatheringPointCreateByCurrentUser, db: Session):
        user = AuthController.getUserByEmail(gathering_point.user_email, db)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User not found",
            )
        new_gathering_point = GatheringPointModel(
            name=gathering_point.name,
            address=gathering_point.address,
            phone=gathering_point.phone,
        )
        db.add(new_gathering_point)
        db.commit()
        db.refresh(new_gathering_point)
        new_gathering_leader = GatheringLeaderModel(
            user_id=user.id,
            gathering_point_id=new_gathering_point.id,
        )
        user.role = UserRoles.GATHERING_LEADER
        db.add(new_gathering_leader)
        db.commit()
        db.refresh(new_gathering_leader)
        return new_gathering_point
    
    def createTransactionPointByCurrentUser(transaction_point: TransactionPointCreateByCurrentUser, db: Session):
        user = AuthController.getUserByEmail(transaction_point.user_email, db)
        if user is None:
            print("User not found")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User not found",
            )
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
        new_transaction_leader = TransactionLeaderModel(
            user_id=user.id,
            transaction_point_id=new_transaction_point.id,
        )
        user.role = UserRoles.TRANSACTION_LEADER
        db.add(new_transaction_leader)
        db.commit()
        db.refresh(new_transaction_leader)
        return new_transaction_point

    def deleteGatheringLeader(gathering_leader_id: int, db: Session):
        gathering_leader = (
            db.query(GatheringLeaderModel)
            .filter(GatheringLeaderModel.id == gathering_leader_id)
            .first()
        )
        if not gathering_leader:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Gathering leader not found",
            )
        db.delete(gathering_leader)
        db.commit()
        return gathering_leader

    def deleteTransactionLeader(transaction_leader_id: int, db: Session):
        transaction_leader = (
            db.query(TransactionLeaderModel)
            .filter(TransactionLeaderModel.id == transaction_leader_id)
            .first()
        )
        if not transaction_leader:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Transaction leader not found",
            )
        db.delete(transaction_leader)
        db.commit()
        return transaction_leader

    def deleteGatheringStaff(gathering_staff_id: int, db: Session):
        gathering_staff = (
            db.query(GatheringStaffModel)
            .filter(GatheringStaffModel.id == gathering_staff_id)
            .first()
        )
        if not gathering_staff:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Gathering staff not found",
            )
        db.delete(gathering_staff)
        db.commit()
        return gathering_staff

    def deleteTransactionStaff(transaction_staff_id: int, db: Session):
        transaction_staff = (
            db.query(TransactionStaffModel)
            .filter(TransactionStaffModel.id == transaction_staff_id)
            .first()
        )
        if not transaction_staff:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Transaction staff not found",
            )
        db.delete(transaction_staff)
        db.commit()
        return transaction_staff
