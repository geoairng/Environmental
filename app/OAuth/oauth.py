from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends, status
import jwt
from jwt.exceptions import InvalidTokenError
from typing import Dict
from sqlmodel import Session, select
from pydantic import EmailStr
from app.config.config import setting
from app.models.users import Company
from datetime import timedelta, datetime
from app.database.db import get_session


oauth_data = OAuth2PasswordBearer(tokenUrl = "login")
BLACKLIST= set()


class Token:

    def get_access_token(self, payload: Dict):

        data = payload.copy()
        data["exp"] = datetime.utcnow() + timedelta(minutes = setting.expiry_time)

        token: str = jwt.encode(data, setting.secret_key, algorithm = setting.algorithm)
        
        return token
    
    def verify_access_token(self, token: str, credentials_exception):
        try:

            if token in BLACKLIST:
               raise credentials_exception

            data = jwt.decode(token, setting.secret_key, algorithms=[setting.algorithm])
            email : EmailStr = data.get("email")
            if not email:
                raise credentials_exception

        except InvalidTokenError:
            raise credentials_exception
        return email
    
    async def get_current_company(self, token: str = Depends(oauth_data), db: Session = Depends(get_session)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},)
         
        email: EmailStr = self.verify_access_token(token, credentials_exception)
       
        company = await db.exec(select(Company).where(Company.company_email == email))
        company: Company = company.first()
        return company





Token_Data = Token()