from sqlalchemy import Column, String, Integer  # Import column types for SQLAlchemy models
from sqlalchemy import create_engine  # Import the function to create a database engine
from sqlalchemy.ext.declarative import declarative_base  # Import the base class for SQLAlchemy models
from sqlalchemy.orm import sessionmaker  # Import session maker to handle database sessions

from pydantic import BaseModel  # Import Pydantic for data validation and serialization
from fastapi import FastAPI  # Import FastAPI to create the API
from crouton import SQLAlchemyCRUDRouter  # Import Crouton to generate CRUD routes

# Initialize the FastAPI application
app = FastAPI()

# Create a SQLite database engine with a specific database file and settings
engine = create_engine(
    "sqlite:///./app.db",  # Define the SQLite database file path
    connect_args={"check_same_thread": False}  # Allow multiple threads to access the database
)

# Configure a session maker to interact with the database
SessionLocal = sessionmaker(
    autocommit=False,  # Disable auto-commit to manage transactions manually
    autoflush=False,  # Disable auto-flush to prevent premature database writes
    bind=engine  # Bind the session maker to the SQLite engine
)

# Create a base class for SQLAlchemy models
Base = declarative_base()

# Define a function to provide database sessions for API routes
def get_db():
    session = SessionLocal()  # Create a new database session
    try:
        yield session  # Yield the session for use in API routes
        session.commit()  # Commit the session after successful use
    finally:
        session.close()  # Ensure the session is closed to release resources

# Define the Pydantic schema for creating a company
class CompanyCreate(BaseModel):
    name: str  # The name of the company as a string
    location: str  # The location of the company as a string
    employee_number: int  # The number of employees in the company as an integer

# Define the Pydantic schema for returning a company, extending the create schema
class Company(CompanyCreate):
    id: int  # The unique identifier for the company as an integer

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models

# Define the SQLAlchemy model for the company database table
class CompanyModel(Base):
    __tablename__ = 'companies'  # Define the table name in the database
    id = Column(Integer, primary_key=True, index=True)  # Define the primary key column with an index
    name = Column(String)  # Define the name column as a string
    location = Column(String)  # Define the location column as a string
    employee_number = Column(Integer)  # Define the employee number column as an integer

# Create the database tables based on the SQLAlchemy models
Base.metadata.create_all(bind=engine)

# Create a CRUD router for the company model using Crouton
router = SQLAlchemyCRUDRouter(
    schema=Company,  # Use the Company schema for validation
    create_schema=CompanyCreate,  # Use the CompanyCreate schema for creation
    db_model=CompanyModel,  # Use the CompanyModel as the database model
    db=get_db,  # Use the database session provider
    prefix='company'  # Define the route prefix as 'company'
)

# Include the CRUD router in the FastAPI application
app.include_router(router)
