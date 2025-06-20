from fastapi import APIRouter, Response
from server.models.user import NewUser, LoginRequest
from server.controller.user import signup, login, logout, get_profile

user_router = APIRouter()

@user_router.post("/signup")
async def signup(user: NewUser):
        return await signup(user)

@user_router.post('/login')
async def login(login_data : LoginRequest, response : Response):
    return await login(login_data, response)

@user_router.get("/logout")
async def logout(response: Response):
    return await logout(response)

@user_router.get("/profile")
async def get_profile():
    return await get_profile()




# @router.patch("/modify_user/{user_id}")
# async def update_user(user_id: int, newinfo: dict):
#     try:
#         await update_user_info(user_id, user_db_client[USER_DATABASE_NAME][USER_COLLECTION], newinfo)
#         return {"user_id": str(user_id)}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))