from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .router import login, users, facility

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

app.include_router(login.app)
app.include_router(users.app)
app.include_router(facility.app)

@app.get('/')
async def hello():
    return 'hi, Successful'