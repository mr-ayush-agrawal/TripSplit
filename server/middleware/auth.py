from fastapi import Depends, HTTPException, status, Request
from server.utils.jwt_auth import verify_token
from shared.cookie import LOGIN_COOKIE_NAME
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM")

async def is_logged_in(request: Request):
    token = request.cookies.get(LOGIN_COOKIE_NAME)

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing authentication token"
        )

    payload = verify_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    return payload