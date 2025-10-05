# api/main.py
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from src.logic import DonationHub 
hub = DonationHub()

app = FastAPI(title="Donation Tracker", version="1.0")

# ✅ Add this CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------- Pydantic Models ----------------
class User(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    role: Optional[str]
    phone: Optional[str]
    city: Optional[str]


class Requirement(BaseModel):
    req_id: Optional[int] 
    ngo_id: int
    item_type: str
    description: str
    quantity: int
    deadline: Optional[str]
class Donation(BaseModel):
    donation_id: Optional[int] = None  # default to None
    donor_id: int
    req_id: int
    item_type: str
    quantity: int
    donation_date: Optional[str] = None
    pickup_address: Optional[str] = None
    delivery_date: Optional[str] = None



# ---------------- USERS ----------------

@app.post("/users")
def create_user(user: User):
    try:
        return hub.add_user(user.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/users")
def get_all_users():
    return hub.list_users()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return hub.get_user_by_id(user_id)

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return hub.update_user(user_id, user.dict(exclude_unset=True))


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return hub.delete_user(user_id)

# ---------------- REQUIREMENTS ----------------
@app.post("/requirements")
def create_requirement(req: Requirement):
    return hub.add_requirement(req.dict())

@app.get("/requirements")
def get_all_requirements():
    return hub.list_requirements()

@app.get("/requirements/{req_id}")
def get_requirement(req_id: int):
    return hub.get_requirement_by_id(req_id)

@app.put("/requirements/{req_id}")
def update_requirement(req_id: int, req: Requirement):
    return hub.update_requirement(req_id, req.dict(exclude_unset=True))

@app.delete("/requirements/{req_id}")
def delete_requirement(req_id: int):
    return hub.delete_requirement(req_id)

# ---------------- DONATIONS ----------------
@app.post("/donations")
def create_donation(donation: Donation):
    return hub.add_donation(donation.dict())

@app.get("/donations")
def get_all_donations():
    return hub.list_donations()

@app.get("/donations/{donation_id}")
def get_donation(donation_id: int):
    return hub.get_donation_by_id(donation_id)

@app.put("/donations/{donation_id}")
def update_donation(donation_id: int, donation: Donation):
    return hub.update_donation(donation_id, donation.dict(exclude_unset=True))

@app.delete("/donations/{donation_id}")
def delete_donation(donation_id: int):
    return hub.delete_donation(donation_id)

@app.put("/donations/{donation_id}/complete")
def mark_completed(donation_id: int, delivery_date: str = Body(..., embed=True)):
    return hub.mark_donation_completed(donation_id, delivery_date)
