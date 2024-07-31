from sqlmodel import SQLModel

from sqlmodel import Field, Relationship
from typing import Optional,List, TYPE_CHECKING
from pydantic import EmailStr
import sqlalchemy
from datetime import datetime
from typing import Optional


if TYPE_CHECKING:
    from .facility import Facility



class Company(SQLModel, table= True):
    id: Optional[int] = Field(primary_key = True, default = None)
    company_email: EmailStr = Field(unique = True)
    company_name: str
    password: str
    location: str = None
    facility: Optional["Facility"] = Relationship(back_populates= "company", sa_relationship_kwargs={'lazy': 'selectin'})
    created_at: datetime = Field(default_factory=datetime.utcnow, sa_column=sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.utcnow))
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column=sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow))




class LoginCred(SQLModel):
    access_token: str
    token_type: str

class PasswordData(SQLModel):
    old_password: str
    new_password: str
    confirm_newpassword: str

class PlainText(SQLModel):
    detail: str

class ForgetPassword(SQLModel):
    company_email: EmailStr

class CreateCompany(SQLModel):
    company_email: EmailStr
    password: str
    confirm_password: str
    company_name: str
    location: str

class CompanyOut(SQLModel):
    id: int
    company_email: EmailStr
    company_name: str
    location: str
    created_at: datetime
    updated_at: datetime

#class UserData(UserOut):
    #companies: List[CompanyOut]
    