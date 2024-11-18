# Mini Loan App

Welcome to the **Mini Loan App**! This project is a full-stack web application built using **Django** for the backend and **React** for the frontend. The application is hosted on **AWS** and is designed to facilitate loan management, allowing users to register, apply for loans, and make repayments, with administrative functionality to approve loans. This repository hosts the backend code.

- **Backend**: Django REST Framework, JWT Authentication
- **Frontend**: React.js
- **Hosting**: AWS Server
- **Live Demo**: [http://54.252.194.42:8000/](http://54.252.194.42:8000/)

---

## Project Overview

The Mini Loan App consists of a backend REST API service and a modern React.js frontend. The project aims to provide an easy-to-use interface for managing loans while incorporating robust security measures like JWT authentication.

---

## Key Features

### User Authentication
- Register and login functionality with password confirmation.
- JWT-based token management for secure access.
- Admin-only access to functionalities such as loan approval.

### Loan Management
- Users can apply for loans, view loan details, and make repayments.
- Admin users have the ability to approve or reject loan requests.

### Scheduled Repayments
- Users can view the repayment schedule and make payments for their loans.

---

## Approach & Design

### Backend (Django)
The backend was developed using Django REST Framework (DRF), with JWT used for secure authentication. Below is an outline of the core features:

#### API Endpoints
- **Register User**: Allows new users to sign up.
- **User Login**: Authenticate users and provide JWT tokens.
- **User Profile**: Retrieve authenticated user profile details.
- **Loan Creation**: Users can create loan requests with specified amounts and terms.
- **Loan Listing**: Fetch all loans associated with the logged-in user.
- **Loan Approval**: Admin-only endpoint to approve loans.
- **Repayment Schedule**: View repayments for a particular loan.
- **Make Repayment**: Users can make repayments against their loans.

#### Data Flow
- A robust database schema manages user information, loans, and repayment schedules.
- Implemented secure routes using JWT authentication.

---

### Frontend (React.js)
The frontend was built using **React**, with React Router for route handling and Context API for global state management (authentication and loan details). It features a clean, intuitive interface with protected routes.

- **Frontend Repository**: [LoanApp-Frontend](https://github.com/itsashishrath/LoanApp-Frontend)

---

## Security Measures
- **JWT Authentication**: Used for securing API endpoints and ensuring token refresh capabilities.
- **Admin Access Control**: Admin functionalities are restricted to authorized users, utilizing React's routing and context features.

---

## Installation & Setup Guide

### Backend Setup (Django)
1. **Clone the backend repository**:
   ```bash
   git clone https://github.com/itsashishrath/LoanApp-Frontend.git
   cd LoanApp-Frontend
   git clone https://github.com/itsashishrath/LoanApp-Frontend.git
   cd LoanApp-Frontend
   ```
2. **Create a virtual environment**:
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows:
    venv\Scripts\activate  # linux
```
3. **Install dependencies**:
```bash
    pip install -r requirements.txt
```

4. **Apply database migrations**:

```bash

python manage.py makemigrations
python manage.py migrate
```

5. **Run the development server**:

```bash
python manage.py runserver localhost:8000
Note: Using localhost:8000 is crucial due to allowed host settings and CORS configurations.
```


**Frontend Setup (React)**
```bash
Instructions for setting up the frontend are available in the frontend repository.

Clone the frontend repository.

Install dependencies using npm install.

Run the frontend server using npm start.
```

**How to Use the Application**

**1. User Flow**
```bash
Registration: Users can sign up on the registration page.
Login: Obtain a JWT token to access protected routes.
Profile: View and update user profile details.
Loan Management: Apply for new loans, view existing loans, and make repayments.
Admin Dashboard: Admin users can log in to approve or manage loans.
API Testing
To test the backend APIs, use tools like curl or Postman. Here's a brief description of how to use some of the key endpoints:

Register a New User: POST /auth/register/
Login: POST /auth/login/
Get User Profile: GET /auth/profile/ (with Authorization: Bearer <JWT_TOKEN>)
Create Loan: POST /loans/
Approve Loan (Admin): POST /loans/<id>/approve/
Refer to the code snippets in the project for full usage.
```
