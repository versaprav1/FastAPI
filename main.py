from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.interfaces import router as interfaces_router

app = FastAPI(title="Interface Data API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(interfaces_router)

@app.get("/")
async def root():
    return {"message": "Welcome to Interface Data API"}