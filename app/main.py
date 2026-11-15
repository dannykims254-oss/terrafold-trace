
from fastapi import FastAPI

# Import farmer routes
from app.routes import farmers

# Import database configuration
from app.core.database import engine, Base

# Import database models
from app.models.farmer import Farmer


# Create database tables
Base.metadata.create_all(bind=engine)


# Initialize TerraFold Trace
app = FastAPI(
    title="TerraFold Trace",
    description=(
        "Agricultural Digital Infrastructure "
        "and Intelligence Platform"
    ),
    version="0.2.0"
)


# Register application modules
app.include_router(farmers.router)


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to TerraFold Trace",
        "platform": "Agricultural Digital Infrastructure",
        "company": "TerraFold Trace Ltd",
        "status": "Operational"
    }


# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "TerraFold Trace",
        "database": "configured"
    }
