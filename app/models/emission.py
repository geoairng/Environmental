from sqlmodel import Field, Relationship, SQLModel
from typing import Optional, List, TYPE_CHECKING
import sqlalchemy
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey
from typing import Optional


if TYPE_CHECKING:
    
    from .facility import Facility



class Emission(SQLModel, table= True):
    id: Optional[int] = Field(primary_key = True, default = None)
    type: str
    amount: float
    facility_id: int = Field(sa_column= Column(Integer, 
    ForeignKey("facility.id", ondelete="CASCADE"), nullable= False), default = None)
    facility: List["Facility"] = Relationship(back_populates= "emissions", sa_relationship_kwargs={'lazy': 'selectin'})
    created_at: datetime = Field(default_factory=datetime.utcnow, sa_column=sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.utcnow))
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column=sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow))





