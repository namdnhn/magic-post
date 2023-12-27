from datetime import datetime, timedelta
from jwt import PyJWTError
import jwt
from sqlalchemy.orm import Session
from database import getDatabase
from fastapi.security import HTTPBearer
from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
from models.user import UserModel, UserDetailModel
from schemas.userSchema import (
    ConfirmPassword,
    RegisterUser,
    Login,
    UpdateUser,
)
from dotenv import load_dotenv
import os
from fastapi.security import HTTPBearer

load_dotenv()

# token
reusable_oauth2 = HTTPBearer(scheme_name="Authorization")
token_blacklist = set()


def createAccessToken(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        days=int(os.getenv("ACCESS_TOKEN_EXPIRE_DAYS"))
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM")
    )
    return encoded_jwt


def isTokenInvalidated(token=Depends(reusable_oauth2)):
    if str(token) in token_blacklist:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has been invalidated",
        )
    return True


def verifyToken(db: Session = Depends(getDatabase), data=Depends(reusable_oauth2)):
    try:
        isTokenInvalidated(token=data)
        payload = jwt.decode(
            data.credentials, os.getenv("SECRET_KEY"), algorithms=os.getenv("ALGORITHM")
        )
        user_id: str = payload.get("userId")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate user",
                headers={"WWW-Authenticate": "Bearer"},
            )
        token_data = user_id
    except PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = db.query(UserModel).filter(UserModel.id == token_data).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate user",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


# hashing password
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


def bcrypt(password: str):
    return pwd_cxt.hash(password)


def verify(hashed_password, plain_password):
    return pwd_cxt.verify(plain_password, hashed_password)


class AuthController:
    def getFullnameByUserId(userId: int, db: Session = Depends(getDatabase)):
        dbUserDetailId = (
            db.query(UserDetailModel).filter(UserDetailModel.user_id == userId).first()
        )
        if dbUserDetailId is None:
            return "User not found"
        return dbUserDetailId.fullname
    
    def getAllUser(db: Session):
        return db.query(UserModel).all()

    def getUserByEmail(email: str, db: Session = Depends(getDatabase)):
        return db.query(UserModel).filter(UserModel.email == email).first()

    def getUserById(userId: int, db: Session = Depends(getDatabase)):
        return db.query(UserModel).filter(UserModel.id == userId).first()

    def createUser(user: RegisterUser, db: Session = Depends(getDatabase)):
        is_user_exist = db.query(UserModel).filter(UserModel.email == user.email).first()
        if is_user_exist:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User with email {user.email} already exists",
            )
        try:
            db_user = UserModel(
                email=user.email,
                password=bcrypt(user.password),
                role=user.role,
            )
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            db_user_detail = UserDetailModel(
                user_id = db_user.id,
                gender = user.gender,
                date_of_birth = user.date_of_birth,
                fullname = user.fullname,
                phone = user.phone,
                address = user.address,
                image_path = user.image_path,
            )
            db.add(db_user_detail)
            db.commit()
            db.refresh(db_user_detail)
            access_token = createAccessToken(data={"userId": db_user.id, "role": db_user.role})
            return {
                "user": db_user,
                "user_detail": db_user_detail,
                "jwtToken": access_token,
            }
        except Exception as e:
            print("Lỗi:", e)

    def login(
        request: Login,
        db: Session = Depends(getDatabase),
    ):
        user = db.query(UserModel).filter(UserModel.email == request.email).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
            )
        if not verify(user.password, request.password):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password"
            )

        access_token = createAccessToken(data={"userId": user.id, "role": user.role})

        response = {
            "id": user.id,
            "email": user.email,
            "role": user.role,
            "access_token": access_token,
        }
        return response

    def logout(token: str = Depends(reusable_oauth2)):
        try:
            verifyToken
            token_blacklist.add(str(token))
            return {"msg": "You have been logged out"}
        except PyJWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

    def updateUser(userId: int, user: UpdateUser, db: Session):
        dbUserId = db.query(UserModel).filter(UserModel.id == userId).first()
        dbUserDetailId = (
            db.query(UserDetailModel).filter(UserDetailModel.user_id == userId).first()
        )
        if not verify(dbUserId.password, user.currentPass):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password"
            )
        if user.fullname is not None:
            dbUserDetailId.fullname = user.fullname
        if user.email is not None:
            dbUserId.email = user.email
        if user.newPassword is not None:
            dbUserId.password = bcrypt(user.newPassword)
        if user.date_of_birth is not None:
            dbUserDetailId.date_of_birth = user.date_of_birth
        if user.role is not None:
            dbUserId.role = user.role
        if user.gender is not None:
            dbUserDetailId.gender = user.gender
        if user.phone is not None:
            dbUserDetailId.phone = user.phone
        if user.address is not None:
            dbUserDetailId.address = user.address
        if user.image_path is not None:
            dbUserDetailId.image_path = user.image_path
        db.commit()
        return {"msg": "Updated"}

    def deleteUser(userId: int, password: ConfirmPassword, db: Session):
        dbUserId = db.query(UserModel).filter(UserModel.id == userId).first()
        if not verify(dbUserId.password, password.currentPass):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password"
            )
        dbUserId = db.query(UserModel).filter(UserModel.id == userId).first()
        dbUserDetailId = (
            db.query(UserDetailModel).filter(UserDetailModel.user_id == userId).first()
        )
        db.delete(dbUserId)
        db.delete(dbUserDetailId)
        db.commit()
        return {"msg": "Deleted"}
    
    def isLoggedIn(token: str = Depends(reusable_oauth2)):
        try:
            verifyToken
            return {"msg": "You have been logged in"}
        except PyJWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
