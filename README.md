# Donation Hub

The Donation Hub is a web-based platform designed to streamline the process of donating and managing contributions to NGOs and charitable organizations. It allows donors to contribute items such as clothes, food, or money and enables NGOs to post their requirements, accept donations, and track the progress of these donations.

The system ensures transparency and accountability by providing donors and NGOs with real-time updates on donation statuses, helping both parties manage resources efficiently. By digitizing the donation process, this system reduces manual record-keeping, minimizes errors, and encourages more people to participate in charitable activities.

## Key Features
# For Donors

Register/Login to the system.

View NGO requirements (items needed, quantity, deadline).

Donate items (clothes, food, money).

Track donation status: Pending → Accepted → Delivered.

View donation history.

# For NGOs

Register/Login to the system.

Post new donation requirements with description, type, and quantity.

View incoming donations and accept/reject them.

Update donation fulfillment status.

# System Features

Manage users (Donors, NGOs, Admin).

Match donations to requirements automatically.

Generate reports on donations and fulfilled requirements.

## Project Structure
Donation Tracker/
|
|---src/           #core application logic
|   |---logic.py   #business logic and task
operations
|   |__db.py       #Database Operations
|
|---api/            #Backend API
|   |__main.py      #FastAPI endpoints
|
|---frontend/       #Frontend Application
|   |__app.py       #Streamlit web interface
|
|___requirements.txt   #Python Dependencies
|
|___README.md         #Project Documentation
|
|___.env        #Python variables

## Quick start

## Prerequisites
Python 3.8 or higher
A Supabase Account
Git(push,cloning)

# 1.clone or Download the Project
# option 1:clone with git
git clone
# option 2:Download and extract the zip files

### 2.Install Dependencies

# Install all required Python packages
pip install -r requirements.txt

## 3.Setup Supabase Database
1.Create a Supabase Project
2.Create the Tasks Table:
-Go to the SQL Editor in your Supabase dashboard
-Run this SQL Command

```sql
Users(
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(20) CHECK(role IN ('donor','ngo','admin')),
    phone VARCHAR(15),
    city VARCHAR(50)
);

Requirements(
    req_id INT PRIMARY KEY,
    ngo_id INT,
    item_type VARCHAR(50),       -- e.g., clothes, food, money
    description TEXT,
    quantity INT,
    deadline DATE,
    status VARCHAR(20) DEFAULT 'open', -- open, fulfilled, closed
    FOREIGN KEY (ngo_id) REFERENCES Users(user_id)
);

Donations(
    donation_id INT PRIMARY KEY,
    donor_id INT,
    req_id INT,
    item_type VARCHAR(50),
    quantity INT,
    status VARCHAR(20) DEFAULT 'pending', -- pending, accepted, delivered
    donation_date DATE,
    pickup_address TEXT,       -- optional, store here instead of separate table
    delivery_date DATE         -- optional
);

``` 
3.** Get your Credentials:

### 4.Configure Environment Variables
1.Create a `.env` file in the project root
2.Add your Supabase credentials to `.env`:
SUPABASE_URL="https://vrosjkfjgkafjtvgdtns.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZyb3Nqa2ZqZ2thZmp0dmdkdG5zIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODE4NzMsImV4cCI6MjA3MzY1Nzg3M30.8ry9kwedzg_jKVSPdVTC_-Ci1YyuqbPqVs9XATwa0RI"

### 5.Run the Application

## Streamlit Frontend
streamlit run frontend/app.py

## FastAPI Backend
cd api
python main.py

## How to use
1.Donors:
-Login/Register  Browse requirements → Donate → Track status → View history.

2.NGOs:
-Login/Register → Post requirements → Accept/reject donations → Update fulfillment status.

## Technical Details

## Technologies Used

**Frontend**:Streamlit(Python web framework)
**Backend**:FastAPI (Python REST API framework)
**Database**:Supabase (PostgreSQL-based backend-as-a-service)
**Languages**:Python, SQL

### Key Components
1.User Authentication & Role Management
2.Donation & Requirement Matching System
3.Donation Tracking Module
4.Reporting & Analytics

## Troubleshooting
## Common Issues
-Streamlit not running: Check Python version and install dependencies.
-Supabase connection errors: Verify .env credentials and internet connectivity.
-Duplicate entries: Ensure unique constraints in tables (email, IDs).

## Future Enhancements

-Notification System: Email/SMS alerts for donation updates.
-Geolocation Integration: Map-based donor-NGO matching.
-Multiple Payment Gateways: For monetary donations.
-Admin Dashboard: Enhanced analytics with charts and graphs.
-Mobile App Version: Android/iOS app for easier access.
-Donation Pickup Scheduling: Integrate logistics for item collection.
-AI-based Matching: Prioritize urgent NGO requirements.
## Support
If you encounter any issue or have questions: dendidivya1102@gmail.com & 7396820680


