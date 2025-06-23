from fastapi import APIRouter, Response, Depends
from server.models.user import NewUser, LoginRequest
from server.controller.user import signup, login, logout, get_profile
from server.middleware.auth import is_logged_in

user_router = APIRouter()

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




# @router.patch("/modify_user/{user_id}")
# async def update_user(user_id: int, newinfo: dict):
#     try:
#         await update_user_info(user_id, user_db_client[USER_DATABASE_NAME][USER_COLLECTION], newinfo)
#         return {"user_id": str(user_id)}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))