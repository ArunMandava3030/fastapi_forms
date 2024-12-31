# FastAPI Forms

FastAPI Forms is a backend application built using FastAPI that enables users to create, manage, and share dynamic forms. It supports session-based authentication for user security and allows public users to fill and submit forms.

---

## Features

### Authentication
- User Registration
- User Login and Logout

### Form Management
- Create, Retrieve, Update, and Delete forms
- Dynamic fields with various input types (string, number, boolean)

### Form Submissions
- Submit responses to forms
- Retrieve and paginate form submissions

### Database
- PostgreSQL for reliable and scalable data storage

---

## Tech Stack

- Framework: FastAPI
- Authentication: Session-based
- Database ORM: SQLAlchemy
- Database: PostgreSQL
- Validation: Pydantic
- Deployment: Docker (for containerized setup)

---

## File Structure

fastapi_forms/  
│  
├── app/  
│   ├── __init__.py  
│   ├── main.py          # Application entry point  
│   ├── database.py      # Database setup and initialization  
│   ├── models.py        # SQLAlchemy models for database  
│   ├── schemas.py       # Pydantic schemas for request and response validation  
│   ├── auth/  
│   │   ├── __init__.py  
│   │   ├── routes.py    # User authentication routes  
│   │   └── utils.py     # Helper functions for authentication  
│   ├── forms/  
│   │   ├── __init__.py  
│   │   ├── routes.py    # Routes for form management  
│   │   └── submissions.py  # Routes for form submissions  
│   └── utils.py         # Utility functions for reusable logic  
│  
├── Dockerfile           # Docker image configuration  
├── docker-compose.yml   # Docker Compose setup  
├── requirements.txt     # Python dependencies  
└── README.md            # Project documentation  

---

## API Endpoints

### Authentication Routes
1. **Register User**  
   Route: POST /auth/register  
   Request Body:  
   ```json
   {
       "username": "string",
       "email": "string",
       "password": "string"
   }
   ```

2. **Login User**  
   Route: POST /auth/login  
   Request Body:  
   ```json
   {
       "email": "string",
       "password": "string"
   }
   ```

3. **Logout User**  
   Route: POST /auth/logout  

### Form Management Routes
1. **Create a Form**  
   Route: POST /forms/create  
   Request Body:  
   ```json
   {
       "title": "string",
       "description": "string",
       "fields": [
           {
               "field_id": "string",
               "type": "string",
               "label": "string",
               "required": true
           }
       ]
   }
   ```

2. **Delete a Form**  
   Route: DELETE /forms/delete/{form_id}  

3. **Get All Forms**  
   Route: GET /forms/  

4. **Get a Single Form**  
   Route: GET /forms/{form_id}  

---

### Form Submission Routes
1. **Submit a Form**  
   Route: POST /forms/submit/{form_id}  
   Request Body:  
   ```json
   {
       "responses": [
           {
               "field_id": "string",
               "value": "string"
           }
       ]
   }
   ```

2. **Get Form Submissions**  
   Route: GET /forms/submissions/{form_id}?page=1&limit=10  
   Response:  
   ```json
   {
       "total_count": 25,
       "page": 1,
       "limit": 10,
       "submissions": [
           {
               "submission_id": "12345",
               "submitted_at": "2024-12-27T12:00:00Z",
               "data": {
                   "field_id_1": "value",
                   "field_id_2": 42,
                   "field_id_3": true
               }
           },
           {
               "submission_id": "12346",
               "submitted_at": "2024-12-27T13:00:00Z",
                   "data": {
                       "field_id_1": "another value",
                       "field_id_2": 55,
                       "field_id_3": false
                   }
           }
       ]
   }
   ```

---

## Setup and Run

### 1. Local Development (Without Docker)
#### Prerequisites
- Python >= 3.10
- PostgreSQL

#### Steps
1. Clone the repository:
   ```
   git clone https://github.com/ArunMandava3030/fastapi_forms.git
   cd fastapi_forms
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate       # On Linux/macOS
   venv\Scripts\activate          # On Windows
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Create a PostgreSQL database with the following details (or adjust `DATABASE_URL` in `app/database.py`):
     - Username: `user`
     - Password: `password`
     - Database Name: `fastapi_forms`

5. Run database migrations:
   ```
   python -c "from app.database import init_db; import asyncio; asyncio.run(init_db())"
   ```

6. Start the application:
   ```
   uvicorn app.main:app --reload
   ```

---

### 2. Using Docker
#### Steps
1. Build and start the application:
   ```
   docker-compose up --build
   ```

2. Stop the containers:
   ```
   docker-compose down
   ```

---

## Access the Application
- API Documentation (Swagger): http://127.0.0.1:8000/docs  
- ReDoc Documentation: http://127.0.0.1:8000/redoc  

---

## Contributing
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

---

## License
This project is licensed under the MIT License.


![378118696-abbfb298-f67e-4ba1-9769-c62a65364181](https://github.com/user-attachments/assets/6e2e1068-ccf9-4795-a8dc-b7c1d7a47619)
![378118465-7dbffb5c-99e0-41b4-a5f6-27a5cfcbab7f](https://github.com/user-attachments/assets/433a2d10-1927-4d63-a663-9aec01b9e35d)
