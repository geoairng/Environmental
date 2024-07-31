from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import create_engine, Session, SQLModel, select
from typing import List, Optional
from app.database.db import get_session
from app.models.model import Company, Facility, Emission  # Import your models here

# Initialize FastAPI app
app = APIRouter()


@app.get("/companies", response_model=List[Company])
async def get_companies(db: Session = Depends(get_session)):
    result = await db.exec(select(Company))

    companies = result.scalars().all() # Fetch all results
    if not companies:
        raise HTTPException(404, detail= "No registered company at the moment")

    return companies



@app.get("/companies/{company_id}", response_model=Company)
async def get_company(company_id: int, db: Session = Depends(get_session)):
    
    part_company = await db.get(Company, company_id)
    
    if not part_company:
        raise HTTPException(404, detail= f"No company with an id {id}")
   
    return part_company

@app.get("/companies/{company_id}/facilities", response_model=List[Facility])
async def get_facilities_by_company(company_id: int, db: Session = Depends(get_session)):
    company = await db.get(Company, company_id)
    
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company.facilities

@app.get("/facilities/{facility_id}/emissions", response_model=List[Emission])
async def get_emissions_by_facility_and_gas_type(facility_id: int, gas_type: str, db: Session = Depends(get_session)):
    
    facility = await db.get(Facility, facility_id)
    if not facility:
        raise HTTPException(status_code=404, detail="Facility not found")
    emissions = await db.exec(select(Emission).filter(Emission.facility_id == facility_id,
            Emission.gas_type == gas_type))
    emissions = emissions.all()
    return emissions
