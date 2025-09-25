# db_manager.py
import os
from supabase import create_client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# ---------------- USERS TABLE ----------------
def create_user(user_id, name, email, password, role, phone, city):
    data = {
        "user_id": user_id,
        "name": name,
        "email": email,
        "password": password,
        "role": role,
        "phone": phone,
        "city": city
    }
    return supabase.table("Users").insert(data).execute()

def get_users():
    return supabase.table("Users").select("*").execute()
def get_user_by_email(email):
    return supabase.table("Users").select("*").eq("email", email).single().execute()

def update_user(user_id, update_data: dict):
    return supabase.table("Users").update(update_data).eq("user_id", user_id).execute()

def delete_user(user_id):
    return supabase.table("Users").delete().eq("user_id", user_id).execute()


# ---------------- REQUIREMENTS TABLE ----------------
def create_requirement(req_id, ngo_id, item_type, description, quantity, deadline):
    data = {
        "req_id": req_id,
        "ngo_id": ngo_id,
        "item_type": item_type,
        "description": description,
        "quantity": quantity,
        "deadline": deadline,
        "status": "open"
    }
    return supabase.table("Requirements").insert(data).execute()

def get_requirements():
    return supabase.table("Requirements").select("*").execute()

def get_requirement_by_id(req_id):
    return supabase.table("Requirements").select("*").eq("req_id", req_id).single().execute()

def update_requirement(req_id, update_data: dict):
    return supabase.table("Requirements").update(update_data).eq("req_id", req_id).execute()

def delete_requirement(req_id):
    return supabase.table("Requirements").delete().eq("req_id", req_id).execute()


# ---------------- DONATIONS TABLE ----------------
def create_donation(donation_id, donor_id, req_id, item_type, quantity, donation_date, pickup_address=None, delivery_date=None):
    data = {
        "donation_id": donation_id,
        "donor_id": donor_id,
        "req_id": req_id,
        "item_type": item_type,
        "quantity": quantity,
        "status": "pending",
        "donation_date": donation_date,
        "pickup_address": pickup_address,
        "delivery_date": delivery_date
    }
    return supabase.table("Donations").insert(data).execute()

def get_donations():
    return supabase.table("Donations").select("*").execute()

def get_donation_by_id(donation_id):
    return supabase.table("Donations").select("*").eq("donation_id", donation_id).single().execute()

def update_donation(donation_id, update_data: dict):
    return supabase.table("Donations").update(update_data).eq("donation_id", donation_id).execute()

def delete_donation(donation_id):
    return supabase.table("Donations").delete().eq("donation_id", donation_id).execute()
