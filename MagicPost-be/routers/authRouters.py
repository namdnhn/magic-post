from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from database import getDatabase
from schemas.userSchema import Login, RegisterUser, UpdateUser, ConfirmPassword
from models.user import UserModel
from controllers.AuthController import AuthController
from schemas.userSchema import PreparingLeader

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

@router.post("/login")
def login(
    request: Login,
    db: Session = Depends(getDatabase)
):
    return AuthController.login(request, db)

@router.post("/register")
def register(
    request: RegisterUser,
    db: Session = Depends(getDatabase)
):
    return AuthController.createUser(request, db)

@router.get("/logout")
def logout(response: str = Depends(AuthController.logout)):
    return response

@router.get("/me")
def get_me(current_user: UserModel = Depends(getDatabase)):
    return current_user

@router.get("/users/all")
def get_all_user(db: Session = Depends(getDatabase)):
    return AuthController.getAllUser(db)

@router.get("/users/{userId}")
def get_user_by_id(userId: int, db: Session = Depends(getDatabase)):
    return AuthController.getUserById(userId, db)

@router.get("/users/email/{email}")
def get_user_by_email(email: str, db: Session = Depends(getDatabase)):
    return AuthController.getUserByEmail(email, db)

@router.get("/check_login")
def is_logged_in():
    return AuthController.isLoggedIn()

@router.get("/users_not_leader", response_model=List[PreparingLeader])
def get_users_not_leader(db: Session = Depends(getDatabase)):
    return AuthController.getUsersNotLeader(db)

@router.put("/users/update/{userId}")
def update_user(userId: int, request: UpdateUser, db: Session = Depends(getDatabase)):
    return AuthController.updateUser(userId, request, db)

@router.delete("/users/delete/{userId}")
def delete_user(userId: int, password: ConfirmPassword, db: Session = Depends(getDatabase)):
    return AuthController.deleteUser(userId, password, db)