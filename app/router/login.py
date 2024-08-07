"""from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session, select
from app.models.users import Company, PlainText, LoginCred, ForgetPassword
from app.database.db import get_session
from app.Password_Manager.password import password
from app.OAuth.oauth import Token_Data
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import EmailStr
from sqlalchemy.engine.result import ScalarResult


app = APIRouter(
    tags = ["Login"]
)


#forget password route
@app.post("/forgetpassword", response_model=PlainText)
async def forgetpin(Password:ForgetPassword, db: Session= Depends(get_session)):

    company: ScalarResult= await db.exec(select(Company).where(Company.company_email == Password.company_email))
    company : Company = company.first()
    if not company:
        raise HTTPException(status_code= 409, detail = f"No Company with an email {Password.company_email}")

    company.password = password.hash_ps(company.company_email)
    db.add(company)
    await db.commit()
    await db.refresh(company)
    return PlainText(detail = f"The password has been reset to the company e-mail and you are adviced to change it immediately you login")

#login
@app.post("/login", response_model = LoginCred)
async def Login(details:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_session)):
    company: ScalarResult = await db.exec(select(Company).where(Company.company_email == details.username))
  
    comapany: Company | None = company.first()

    if not company:
        raise HTTPException(status_code= 401, detail = "Incorrect Email or password")
    
    
    if not password.verify_hash(details.password, comapany.password):
        raise HTTPException(status_code= 401, detail = "Incorrect Email or password")
    
    token:str = Token_Data.get_access_token({"email": details.username})
    return LoginCred(access_token = token, token_type = "bearer")"""