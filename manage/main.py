from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.config import settings
from router import stake


app = FastAPI(
    title="Subnet Manager",
    version="0.1.0",
    description="Subnet Manager",
    openapi_url="/openapi.json"
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(stake.router)


@app.get("/")
async def root():
    return {
        "version": "0.1.0",
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=settings.MANAGER_HOST,
        port=settings.MANAGER_PORT,
        reload=settings.MANAGER_DEBUG
    ) 