from fastapi import FastAPI

app = FastAPI(
    title="TerraFold Trace",
    description="Agricultural Digital Infrastructure and Intelligence Platform",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to TerraFold Trace",
        "platform": "Agricultural Digital Infrastructure",
        "status": "Operational"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


from fastapi import FastAPI

# Create the TerraFold Trace application
app = FastAPI(
    title="TerraFold Trace",
    description="Agricultural Digital Infrastructure and Intelligence Platform",
    version="0.1.0"
)


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to TerraFold Trace",
        "platform": "Agricultural Digital Infrastructure",
        "status": "Operational"
    }


# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "TerraFold Trace"
    }

from fastapi import FastAPI

from app.routes import farmers


app = FastAPI(
    title="TerraFold Trace",
    description="Agricultural Digital Infrastructure and Intelligence Platform",
    version="0.1.0"
)


# Register application routes
app.include_router(farmers.router)


@app.get("/")
def home():

    return {
        "message": "Welcome to TerraFold Trace",
        "platform": "Agricultural Digital Infrastructure",
        "status": "Operational"
    }


@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "application": "TerraFold Trace"
    }
