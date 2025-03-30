from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from src.core.auth import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload["sub"]  # Returning the user email
