from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from ..database import get_db
from ..models.inventory import Inventory
from ..models.prescription import Prescription
from ..models.error_log import ErrorLog
from ..utils.auth import get_current_user

router = APIRouter(prefix="/notifications", tags=["notifications"])

@router.get("")
def get_notifications(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    notifications = []
    
    low_stock = db.query(Inventory).filter(Inventory.quantity_in_stock < Inventory.low_stock_threshold).all()
    for item in low_stock:
        drug_name = item.drug.brand_name if item.drug else "Unknown Drug"
        notifications.append({
            "id": f"low_{item.inventory_id}",
            "title": f"Low stock: {drug_name}",
            "time": "Stock: " + str(item.quantity_in_stock) + " remaining",
            "unread": True
        })
        
    pending = db.query(Prescription).filter(Prescription.status == "pending").all()
    for rx in pending:
        patient_name = rx.patient.name if rx.patient else "Unknown Patient"
        notifications.append({
            "id": f"rx_{rx.prescription_id}",
            "title": f"Prescription awaits review",
            "time": f"Patient: {patient_name}",
            "unread": True
        })
        
    errors = db.query(ErrorLog).filter(ErrorLog.resolved_by == None).order_by(ErrorLog.created_at.desc()).limit(5).all()
    for err in errors:
        notifications.append({
            "id": f"err_{err.error_id}",
            "title": f"Error: {err.error_type}",
            "time": err.description[:50],
            "unread": True
        })
        
    return notifications
