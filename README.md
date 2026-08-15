# Pulse-NITK

## Campus Event Management Platform

Pulse-NITK is a campus event management web application designed to connect students and event organizers through a single platform.

Students can discover and book campus events, join waitlists, volunteer for events, communicate with organizers, receive notifications, and view event media. Organizers can create and manage events, handle bookings and volunteers, communicate with participants, and upload event media.

---

## Features

### Student Features

* Student registration and login
* Password reset
* Browse upcoming campus events
* Event booking and ticket cancellation
* Automatic waitlist management
* Volunteer registration
* View volunteer status
* Event-based messaging with organizers
* Image and video viewing
* Notifications
* User profile and ID card
* Google Maps integration for event locations

### Organizer Features

* Organizer registration and login
* Create, edit, and delete events
* Manage event capacity
* View event bookings
* Cancel participant bookings
* Manage waitlisted participants
* Add and remove volunteers
* Accept or reject volunteer requests
* Communicate with participants
* Upload and delete event images/videos
* Download booking reports
* Receive event-related notifications

---

## Tech Stack

### Frontend

* HTML5
* CSS3
* Vanilla JavaScript
* Fetch API
* LocalStorage
* Google Maps JavaScript API

### Backend

* Node.js
* Express.js
* REST APIs
* Multer for file uploads
* CORS
* File System (`fs`)
* JSON-based data persistence

---

## Project Structure

```text
Pulse-NITK/
│
├── frontend/
│   └── frontend.html
│
├── backend/
│   ├── backend.js
│   ├── data.json
│   ├── data.example.json
│   ├── package.json
│   └── package-lock.json
│
├── .gitignore
├── sanitize_data.py
└── README.md
```

---

## Architecture

```text
┌──────────────────────────────┐
│        Frontend              │
│     HTML + CSS + JS          │
└──────────────┬───────────────┘
               │
               │ HTTP / REST API
               ▼
┌──────────────────────────────┐
│       Node.js + Express      │
│          Backend             │
└──────────────┬───────────────┘
               │
       ┌───────┴────────┐
       ▼                ▼
   data.json         uploads/
   Data Store        Media Files
```

The frontend communicates with the Express backend through REST API endpoints using the JavaScript Fetch API.

---

## API Categories

The backend provides APIs for:

* Authentication
* User profiles
* Events
* Tickets and bookings
* Waitlists
* Volunteers
* Notifications
* Messaging
* Media uploads
* Organizer management

---

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/kanchangoyal06/Pulse-NITK.git
cd Pulse-NITK
```

### 2. Install backend dependencies

```bash
cd backend
npm install
```

### 3. Start the backend

```bash
npm start
```

The backend runs on the configured local server port.

### 4. Open the frontend

Open:

```text
frontend/frontend.html
```

in a browser.

---

## Data and Privacy

The repository contains a sanitized example dataset in:

```text
backend/data.example.json
```

Real development data is kept separately in:

```text
backend/data.json
```

The example dataset uses dummy names, emails, phone numbers, passwords, and other identifying information.

---

## Screens and Modules

The application includes:

* Authentication
* Home / Events
* Tickets
* Notifications
* Profile
* Media
* Organizer Dashboard
* Volunteer Management
* Waitlist Management
* Event Messaging
* Event Booking Management

---

## Future Improvements

Possible future improvements include:

* Migration from JSON storage to MongoDB or PostgreSQL
* Secure password hashing
* JWT-based authentication
* Role-based authorization middleware
* Production cloud storage for media
* Improved API validation
* Automated testing
* CI/CD deployment pipeline
* Better scalability and concurrency handling

---

## Author

**Kanchan Goyal**

Pulse-NITK — Campus Event Management Platform

