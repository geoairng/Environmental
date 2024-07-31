from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
from pydantic import EmailStr

class Emission(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    gas_type: str
    value: float
    facility_id: Optional[int] = Field(default=None, foreign_key="facility.id")
    facility: Optional["Facility"] = Relationship(back_populates="emissions")

class Facility(SQLModel, table=True):
    
    id: Optional[int] = Field(default=None, primary_key=True)
    location_bounds: Optional[str] = Field(default=None)  # Using text to store WKT
    company_id: Optional[int] = Field(default=None, foreign_key="company.id")
    company: Optional["Company"] = Relationship(back_populates="facilities")
    emissions: List[Emission] = Relationship(back_populates="facility")

class Company(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: EmailStr
    facilities: List[Facility] = Relationship(back_populates="company")
