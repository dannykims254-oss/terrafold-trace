
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from datetime import datetime, timezone

from app.core.database import Base


class Farm(Base):
    __tablename__ = "farms"

    farm_id = Column(String, primary_key=True, index=True)

    farmer_id = Column(
        String,
        ForeignKey("farmers.farmer_id"),
        nullable=False,
        index=True
    )

    farm_name = Column(String(100), nullable=False)

    county = Column(String(100), nullable=False)

    sub_county = Column(String(100), nullable=False)

    village = Column(String(100), nullable=False)

    farm_size_acres = Column(Float, nullable=False)

    latitude = Column(Float, nullable=True)

    longitude = Column(Float, nullable=True)

    registered_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
