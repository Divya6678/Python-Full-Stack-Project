# frontend/app.py
import streamlit as st
import requests
from datetime import datetime

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Donation Hub", page_icon="🎁", layout="wide")
st.title("🎁 Donation Hub Dashboard")

# ------------------ Sidebar ------------------
st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to", ["Users", "Requirements", "Donations"])

# ------------------ USERS ------------------
if option == "Users":
    st.header("Users")

    # Add User
    st.subheader("Add User")
    with st.form("add_user_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        role = st.selectbox("Role", ["donor", "ngo"])
        phone = st.text_input("Phone")
        city = st.text_input("City")
        submitted = st.form_submit_button("Add User")

        if submitted:
            payload = {
                "name": name,
                "email": email,
                "password": password,
                "role": role,
                "phone": phone,
                "city": city
            }
            res = requests.post(f"{API_URL}/users", json=payload)
            if res.status_code in [200, 201]:
                st.success("User added successfully!")
            else:
                st.error(res.text)

    # List Users
    st.subheader("All Users")
    try:
        res = requests.get(f"{API_URL}/users")
        users = res.json()
        st.table(users)
    except requests.exceptions.ConnectionError:
        st.error("Backend not running. Start FastAPI at port 8000.")

# ------------------ REQUIREMENTS ------------------
elif option == "Requirements":
    st.header("Requirements")

    # Add Requirement
    st.subheader("Add Requirement")
    with st.form("add_req_form"):
        ngo_id = st.number_input("NGO ID", min_value=1)
        item_type = st.text_input("Item Type")
        description = st.text_area("Description")
        quantity = st.number_input("Quantity", min_value=1)
        deadline = st.date_input("Deadline")
        submitted = st.form_submit_button("Add Requirement")

        if submitted:
            payload = {
                "ngo_id": ngo_id,
                "item_type": item_type,
                "description": description,
                "quantity": quantity,
                "deadline": deadline.strftime("%Y-%m-%d")
            }
            res = requests.post(f"{API_URL}/requirements", json=payload)
            if res.status_code in [200, 201]:
                st.success("Requirement added successfully!")
            else:
                st.error(res.text)

    # List Requirements
    st.subheader("All Requirements")
    try:
        res = requests.get(f"{API_URL}/requirements")
        reqs = res.json()
        st.table(reqs)
    except requests.exceptions.ConnectionError:
        st.error("Backend not running.")

# ------------------ DONATIONS ------------------
elif option == "Donations":
    st.header("Donations")

    # Add Donation
    st.subheader("Add Donation")
    with st.form("add_donation_form"):
        donor_id = st.number_input("Donor ID", min_value=1)
        req_id = st.number_input("Requirement ID", min_value=1)
        item_type = st.text_input("Item Type")
        quantity = st.number_input("Quantity", min_value=1)
        donation_date = st.date_input("Donation Date")
        pickup_address = st.text_input("Pickup Address (Optional)")
        submitted = st.form_submit_button("Add Donation")

        if submitted:
            payload = {
                "donor_id": donor_id,
                "req_id": req_id,
                "item_type": item_type,
                "quantity": quantity,
                "donation_date": donation_date.strftime("%Y-%m-%d"),
                "pickup_address": pickup_address or None
            }
            res = requests.post(f"{API_URL}/donations", json=payload)
            if res.status_code in [200, 201]:
                st.success("Donation added successfully!")
            else:
                st.error(res.text)

    # List Donations
    st.subheader("All Donations")
    try:
        res = requests.get(f"{API_URL}/donations")
        donations = res.json()
        st.table(donations)
    except requests.exceptions.ConnectionError:
        st.error("Backend not running.")

    # Mark Donation as Completed
    st.subheader("Mark Donation as Completed")
    donation_id = st.number_input("Donation ID", min_value=1)
    delivery_date = st.date_input("Delivery Date")
    if st.button("Mark Completed"):
        payload = {"delivery_date": delivery_date.strftime("%Y-%m-%d")}
        res = requests.put(f"{API_URL}/donations/{donation_id}/complete", json=payload)
        if res.status_code in [200, 201]:
            st.success("Success!")
        else:
            try:
                error_message = res.json().get("detail", res.text)
            except:
                error_message = res.text
            st.error(f"Error: {error_message}")

