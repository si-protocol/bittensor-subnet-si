from datetime import datetime, timedelta
from typing import Optional
import jwt

from services.config import settings


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create a new JWT access token.
    
    Args:
        data (dict): The data to encode in the token.
        expires_delta (timedelta, optional): Token expiration time.
        
    Returns:
        str: The encoded JWT token.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.SI_API_JWT_EXPIRE_IN)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SI_API_JWT_SECRET_KEY, algorithm=settings.SI_API_JWT_ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> Optional[dict]:
    """Verify a JWT token.
    
    Args:
        token (str): The JWT token to verify.
        
    Returns:
        Optional[dict]: The decoded token payload if valid, None otherwise.
    """
    try:
        payload = jwt.decode(token, settings.SI_API_JWT_SECRET_KEY, algorithms=[settings.SI_API_JWT_ALGORITHM])
        return payload
    except Exception as e:
        print(f"Error verifying token: {e}")
        return None