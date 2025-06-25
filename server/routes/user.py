from fastapi import APIRouter, Response, Depends
from server.models.user import *
from server.controller.user import *
from server.middleware.auth import is_logged_in

user_router = APIRouter(tags=["Users"])

@user_router.post("/signup")
async def user_signup(user: NewUser):
        return signup(user)

@user_router.post('/login')
async def user_login(login_data : LoginRequest, response : Response):
    return login(login_data, response)

@user_router.get("/logout")
async def user_logout(response: Response,user=Depends(is_logged_in)):
    return logout(response, user)

@user_router.get("/profile")
async def user_get_profile(user=Depends(is_logged_in)):
    return get_profile(user)

@user_router.patch('/update-info')
async def update_user_info(newinfo: UpdateUserInfo, user = Depends(is_logged_in)):
    return update_info(newinfo, user)

@user_router.put("/update-password")
async def update_user_password(newinfo: UpdatePassword, user=Depends(is_logged_in)):
    return update_password(newinfo, user)