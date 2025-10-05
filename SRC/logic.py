# src/logic.py
from datetime import datetime
from src.db import *

class DonationHub:

    # ---------------- USERS ----------------
    def add_user(self, user:dict):
        return create_user(user)

    def list_users(self):
        return get_users()

    def get_user_by_id(self, user_id):
        return get_user_by_id(user_id)

    def update_user(self, user_id, user):
        return update_user(user_id, user)

    def delete_user(self, user_id):
        return delete_user(user_id)

    # ---------------- REQUIREMENTS ----------------
    def add_requirement(self, req:dict):
        if "deadline" in req and isinstance(req["deadline"], datetime):
            req["deadline"] = req["deadline"].strftime("%Y-%m-%d")
        return create_requirement(req)

    def list_requirements(self):
        return get_requirements()

    def get_requirement_by_id(self, req_id):
        return get_requirement_by_id(req_id)

    def update_requirement(self, req_id, req):
        return update_requirement(req_id, req)

    def delete_requirement(self, req_id):
        return delete_requirement(req_id)

    # ---------------- DONATIONS ----------------
    def add_donation(self, donation:dict):
        if "donation_date" in donation and isinstance(donation["donation_date"], datetime):
            donation["donation_date"] = donation["donation_date"].strftime("%Y-%m-%d")
        if "delivery_date" in donation and isinstance(donation["delivery_date"], datetime):
            donation["delivery_date"] = donation["delivery_date"].strftime("%Y-%m-%d")
        return create_donation(donation)

    def list_donations(self):
        return get_donations()

    def get_donation_by_id(self, donation_id):
        return get_donation_by_id(donation_id)

    def update_donation(self, donation_id, donation):
        return update_donation(donation_id, donation)

    def delete_donation(self, donation_id):
        return delete_donation(donation_id)

    def mark_donation_completed(self, donation_id, delivery_date):
        update_data = {"status": "delivered", "delivery_date": delivery_date}
        return update_donation(donation_id, update_data)
