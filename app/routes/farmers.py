from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from uuid import uuid4

from app.core.database import get_db
from app.models.farmer import Farmer
from app.schemas.farmer import FarmerCreate, FarmerResponse


router = APIRouter(
    prefix="/farmers",
    tags=["Farmers"]
)


@router.post("/", response_model=FarmerResponse, status_code=201)
def register_farmer(
    farmer: FarmerCreate,
    db: Session = Depends(get_db)
):
    existing_farmer = db.query(Farmer).filter(
        Farmer.phone_number == farmer.phone_number
    ).first()

    if existing_farmer:
        raise HTTPException(
            status_code=409,
            detail="This phone number is already registered."
        )

    new_farmer = Farmer(
        farmer_id=f"TF-FARM-{uuid4().hex[:8].upper()}",
        **farmer.model_dump()
    )

    try:
        db.add(new_farmer)
        db.commit()
        db.refresh(new_farmer)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Farmer registration conflicts with an existing record."
        )

    return new_farmer


@router.get("/", response_model=list[FarmerResponse])
def get_farmers(db: Session = Depends(get_db)):
    return db.query(Farmer).all()


@router.get("/{farmer_id}", response_model=FarmerResponse)
def get_farmer(
    farmer_id: str,
    db: Session = Depends(get_db)
):
    farmer = db.query(Farmer).filter(
        Farmer.farmer_id == farmer_id
    ).first()

    if farmer is None:
        raise HTTPException(
            status_code=404,
            detail="Farmer not found."
        )

    return farmer
