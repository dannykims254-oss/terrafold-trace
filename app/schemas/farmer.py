
from pydantic import BaseModel, Field
from datetime import datetime


# Information required when registering a farmer
class FarmerCreate(BaseModel):

    full_name: str = Field(min_length=3, max_length=100)

    phone_number: str = Field(min_length=9, max_length=15)

    county: str

    sub_county: str

    village: str

    farm_size_acres: float = Field(gt=0)

    primary_crop: str


# Information returned after registration
class FarmerResponse(FarmerCreate):

    farmer_id: str

    registered_at: datetime


from fastapi import APIRouter, HTTPException
from datetime import datetime, timezone
from uuid import uuid4

from app.schemas.farmer import FarmerCreate, FarmerResponse


router = APIRouter(
    prefix="/farmers",
    tags=["Farmers"]
)


# Temporary storage for registered farmers
farmers_db = {}


# Register a new farmer
@router.post("/", response_model=FarmerResponse)
def register_farmer(farmer: FarmerCreate):

    # Prevent duplicate phone registrations
    for existing_farmer in farmers_db.values():
        if existing_farmer["phone_number"] == farmer.phone_number:
            raise HTTPException(
                status_code=409,
                detail="A farmer with this phone number is already registered."
            )

    farmer_id = f"TF-FARM-{uuid4().hex[:8].upper()}"

    farmer_record = farmer.model_dump()

    farmer_record["farmer_id"] = farmer_id
    farmer_record["registered_at"] = datetime.now(timezone.utc)

    farmers_db[farmer_id] = farmer_record

    return farmer_record


# Retrieve all registered farmers
@router.get("/", response_model=list[FarmerResponse])
def get_farmers():

    return list(farmers_db.values())


# Retrieve one farmer using their ID
@router.get("/{farmer_id}", response_model=FarmerResponse)
def get_farmer(farmer_id: str):

    farmer = farmers_db.get(farmer_id)

    if farmer is None:
        raise HTTPException(
            status_code=404,
            detail="Farmer not found."
        )

    return farmer
