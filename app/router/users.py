from fastapi import Depends, APIRouter, HTTPException
from sqlmodel import Session, select
from app.models.users import Company, CreateCompany, CompanyOut, LoginCred, PasswordData, PlainText
from app.database.db import get_session
from app.Password_Manager.password import password
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from app.OAuth.oauth import Token_Data, oauth_data, BLACKLIST
from pydantic import EmailStr
from typing import List

app = APIRouter(
    tags = ["Company"],
    prefix ="/companies"
)

#create account
@app.post("/", response_model = CompanyOut, status_code= 201)
async def create_company(data: CreateCompany, db: Session = Depends(get_session)):

    # if user type the same pasword for the two password field while registering
    if not password.verify_plain(data.confirm_password, data.password):
        raise HTTPException(status_code = 403, detail= f"You didn't enter the same password for password and confirm_password field")
    
    #hash the password
    data.password = password.hash_ps(data.password)

    #check for duplicate email
    company: Company | None = await db.exec(select(Company).where(Company.company_email == data.company_email))
    
    if company.first():
        raise HTTPException(status_code = 409, detail= f"User with email `{data.company_email}` already exist")
   

    # add company to database
    data = Company.from_orm(data)
    db.add(data)
    await db.commit()
    await db.refresh(data)
    
    return data

#get all users
@app.get("/", response_model=List[CompanyOut])
async def get_all_Company(limit:int= 5, offset:int = 0, company: Company = Depends(Token_Data.get_current_company), db: Session = Depends(get_session)):
    members = await db.exec(select(Company).limit(limit).offset(offset).order_by(Company.company_name))
    members:List[Company] |None = members.all()
   

    if not company:
        raise HTTPException(404, detail= f"There is no registered company at the moment")
        
    return members


#change passsword
@app.post("/changepassword", response_model = PlainText)
async def change_password(Password: PasswordData, db: Session = Depends(get_session), company :Company = Depends(Token_Data.get_current_company)):
    if not password.verify_hash(Password.old_password, company.password):
        raise HTTPException(status_code= 409, detail = "You have entered a wrong old password")
    if not password.verify_plain(Password.new_password, Password.confirm_newpassword):
        raise HTTPException(status_code= 409, detail = "New password field and confirm_newpassword field must be the same")
    company.password = password.hash_ps(Password.new_password)
    db.add(company)
    await db.commit()
    await db.refresh(company)
    return PlainText(detail = "Password Changed Successfully")



#get a particular company by id

@app.get("/{id}", response_model = CompanyOut)
async def profile(id: int, company: Company = Depends(Token_Data.get_current_company), db: Session = Depends(get_session)):

    
     
    if id == company.id:
        return company
    part_company = await db.get(Company, id)
    
    if not part_company:
        raise HTTPException(404, detail= f"No company with an id {id}")
   
    return part_company





    

