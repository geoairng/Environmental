from fastapi import Depends, APIRouter, HTTPException
from sqlmodel import Session, select
from app.models.facility import Facility, CreateFacility
from app.models.users import Company
from app.database.db import get_session
from typing import List

app = APIRouter(
    tags = ["Facility"],
    prefix ="/facilities"
)

#create facility
@app.post("/", response_model = Facility, status_code= 201)
async def create_facility(data: CreateFacility, db: Session = Depends(get_session)):


    #check if a company exist
    company: Company| None = await db.exec(select(Company).where(Company.id == data.company_id))
    if not company.first():
        raise HTTPException(status_code = 409, detail= f"No company with the specified ID")

    #check for duplicate facility
    data.facility_type = data.facility_type.lower()
    facility: Facility | None = await db.exec(select(Facility).where(Facility.facility_type == data.facility_type).where(Facility.company_id == data.company_id))
    
    if facility.first():
        raise HTTPException(status_code = 409, detail= f"{data.facility_type} facility already exist in the company")

   
    # add facility to database
    data = Facility.from_orm(data)
    db.add(data)
    await db.commit()
    await db.refresh(data)
    
    return data

#get all facility
@app.get("/", response_model=List[Facility])
async def get_all_facility(limit:int= 5, offset:int = 0, db: Session = Depends(get_session)):
    facility = await db.exec(select(Facility).limit(limit).offset(offset).order_by(Facility.facility_type))
    facility:List[Facility] |None = facility.all()
    if not facility:
        raise HTTPException(404, detail= f"There is no facility at the moment")
        
    return facility


#get a particular facility by type
@app.get("/{facility_type}", response_model = Facility)
async def facility(facility_type: str,  db: Session = Depends(get_session)):

    
     #check if a facility exist
    facility: Facility| None = await db.exec(select(Facility).where(Facility.facility_type == facility_type.lower()))
    if not facility:
        raise HTTPException(status_code = 409, detail= f"This facility does not exist")
    return facility


# check if a particular company has a particular facility
@app.get("/{company_id}", response_model = Facility)
async def company_with_facility(company_id: int, facility_type:str | None= None,  db: Session = Depends(get_session)):

    if not facility_type:
        part_company = await db.get(Company, id)
        if not part_company:
            raise HTTPException(404, detail= f"No company with an id {id}")
        return part_company

    
     #check if a facility exist
    facility: Facility | None = await db.exec(select(Facility).where(Facility.facility_type == facility_type.lower()).where(Facility.company_id == company_id))
    if not facility:
        raise HTTPException(status_code = 409, detail= f"This facility does not exist")
    
    return facility





    

