from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Information required to register a farmer
class FarmerCreate(BaseModel):

    full_name: str = Field(min_length=3, max_length=100)

    phone_number: str = Field(min_length=9, max_length=15)

    county: str = Field(min_length=2)

    sub_county: str = Field(min_length=2)

    village: str = Field(min_length=2)

    farm_size_acres: float = Field(gt=0)

    primary_crop: str = Field(min_length=2)


# Information returned by the API
class FarmerResponse(FarmerCreate):

    farmer_id: str

    registered_at: datetime

    model_config = ConfigDict(from_attributes=True)
