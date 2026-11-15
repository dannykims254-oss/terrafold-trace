from sqlalchemy import Column, String, Float, DateTime
from datetime import datetime, timezone

from app.core.database import Base


class Farmer(Base):
    __tablename__ = "farmers"

    farmer_id = Column(String, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    phone_number = Column(String(15), unique=True, nullable=False)

    county = Column(String(100), nullable=False)

    sub_county = Column(String(100), nullable=False)

    village = Column(String(100), nullable=False)

    farm_size_acres = Column(Float, nullable=False)

    primary_crop = Column(String(100), nullable=False)

    registered_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
