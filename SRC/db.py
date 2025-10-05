# src/db.py
import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Supabase credentials missing in .env")

supabase = create_client(url, key)

# ---------------- USERS ----------------
def create_user(user):
    res = supabase.table("users").insert(user).execute()
    return res.data

def get_users():
    res = supabase.table("users").select("*").execute()
    return res.data

def get_user_by_id(user_id):
    res = supabase.table("users").select("*").eq("user_id", user_id).single().execute()
    return res.data

def update_user(user_id, update_data):
    res = supabase.table("users").update(update_data).eq("user_id", user_id).execute()
    return res.data

def delete_user(user_id):
    res = supabase.table("users").delete().eq("user_id", user_id).execute()
    return res.data


# ---------------- REQUIREMENTS ----------------
def create_requirement(req):
    res = supabase.table("requirements").insert(req).execute()
    return res.data

def get_requirements():
    res = supabase.table("requirements").select("*").execute()
    return res.data
def get_requirement_by_id(req_id):
    res = supabase.table("requirements").select("*").eq("req_id", req_id).single().execute()
    return res.data

def update_requirement(req_id, update_data):
    res = supabase.table("requirements").update(update_data).eq("req_id", req_id).execute()
    return res.data

def delete_requirement(req_id):
    res = supabase.table("requirements").delete().eq("req_id", req_id).execute()
    return res.data


# ---------------- DONATIONS ----------------
def create_donation(donation):
    res = supabase.table("donations").insert(donation).execute()
    return res.data

def get_donations():
    res = supabase.table("donations").select("*").execute()
    return res.data

def get_donation_by_id(donation_id):
    res = supabase.table("donations").select("*").eq("donation_id", donation_id).single().execute()
    return res.data

def update_donation(donation_id, update_data):
    res = supabase.table("donations").update(update_data).eq("donation_id", donation_id).execute()
    return res.data

def delete_donation(donation_id):
    res = supabase.table("donations").delete().eq("donation_id", donation_id).execute()
    return res.data

