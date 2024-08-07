import asyncio
from app.util.util import fetch_weather_data_async, geocode
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import create_engine, Session, SQLModel, select
from typing import List, Optional
from app.database.db import get_session
from app.models.model import Company , EmissionOutPut,Facility, Emission  # Import your models here
import pickle

# Initialize FastAPI app
app = APIRouter()

model_list = ["co2_model.pkl", "nox_model.pkl", "methane_model.pkl"]
model_dict = {1,2,3,4}

for name in model_list:
    with open(f'../../../{name}', 'rb') as model_file:
        model_dict[name[:-4]] = pickle.load(model_file)

@app.get("/emission", response_model = EmissionOutPut)
async def get_emission(gas_type: str, loc: str):

    
    if not gas_type or not loc:
        raise HTTPException(409, detail= "Both gas type and location must be provided to get the emission value")


    if gas_type.lower() not in ["co2","nox", "methane"]:
        raise HTTPException(409, detail= "No data available for the searched gas")

    result = await (geocode(loc))
    if type(result) == dict:
        lat, long = result["lat"],result["long"]
    else:
        raise HTTPException(404, detail= "Geocode failed")
    
    data = await (fetch_weather_data_async(lat, long))

    result = model_dict[f"{gas_type.lower()}_model"].predict(data)
    OutputData = EmissionOutPut(lat = lat, long = long, gas_type = gas_type, emission_value = result[0])
    return OutputData
    
        
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
