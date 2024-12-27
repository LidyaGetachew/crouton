# FastAPI CRUD API with SQLAlchemy and Crouton

This project demonstrates how to build a RESTful API using **FastAPI**, **SQLAlchemy**, and **Crouton** for managing a `Company` entity. The API includes automatically generated CRUD endpoints and uses SQLite as the database.

## Features

- **CRUD Operations**: Create, Read, Update, Delete functionality for the `Company` entity.
- **Database**: Uses SQLAlchemy ORM with SQLite.
- **Validation**: Utilizes Pydantic for input validation and serialization.
- **Auto-Generated Endpoints**: Crouton simplifies the process of creating RESTful routes.
- **Documentation**: Interactive API documentation available via Swagger UI.

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Steps

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API Documentation:**
   Open your browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.

## Project Structure

```
.
├── main.py                # Main application file
├── app.db                 # SQLite database file (generated after running the app)
├── requirements.txt       # Dependencies for the project
└── README.md              # Project documentation
```

## API Endpoints

### CRUD Endpoints

| Method   | Endpoint         | Description                      |
|----------|------------------|----------------------------------|
| `POST`   | `/company/`      | Create a new company             |
| `GET`    | `/company/`      | Retrieve all companies           |
| `GET`    | `/company/{id}`  | Retrieve a specific company by ID|
| `PUT`    | `/company/{id}`  | Update a company by ID           |
| `DELETE` | `/company/{id}`  | Delete a company by ID           |

## Example Request

### Create a Company

**Endpoint:**
```
POST /company/
```

**Payload:**
```json
{
  "name": "Tech Corp",
  "location": "New York",
  "employee_number": 250
}
```

**Response:**
```json
{
  "id": 1,
  "name": "Tech Corp",
  "location": "New York",
  "employee_number": 250
}
```

## Dependencies

- **FastAPI**: Framework for building APIs.
- **SQLAlchemy**: ORM for interacting with the database.
- **Crouton**: For auto-generating CRUD routes.
- **Pydantic**: For validation and serialization.
- **Uvicorn**: ASGI server for running FastAPI apps.


## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Acknowledgements

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Crouton Documentation](https://pypi.org/project/crouton/)
