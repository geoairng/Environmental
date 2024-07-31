"""from sqlmodel import Field, Relationship, SQLModel
from typing import Optional,List, TYPE_CHECKING
import sqlalchemy
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey
from typing import Optional

if TYPE_CHECKING:
    from .users import Company
    from .emission import Emission




class Facility(SQLModel, table= True):
    id: Optional[int] = Field(primary_key = True, default = None)
    location: str
    facility_type: str
    company_id: int = Field(sa_column= Column(Integer, 
    ForeignKey("company.id", ondelete="CASCADE"), nullable= False), default = None)
    company: List["Company"] = Relationship(back_populates= "facility", sa_relationship_kwargs={'lazy': 'selectin'})
    emissions: Optional["Emission"] = Relationship(back_populates= "facility", sa_relationship_kwargs={'lazy': 'selectin'})
    created_at: datetime = Field(default_factory=datetime.utcnow, sa_column=sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.utcnow))
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column=sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow))

class CreateFacility(SQLModel):
    location: str
    facility_type: str
    company_id: int"""


    

    



    