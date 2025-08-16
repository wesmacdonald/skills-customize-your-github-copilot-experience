# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and test RESTful APIs using the FastAPI framework in Python. You will create endpoints, handle requests, and return JSON responses.

## 📝 Tasks

### 🛠️ Task 1: Set Up FastAPI Project

#### Description
Initialize a new FastAPI project and create a basic API endpoint.

#### Requirements
Completed program should:
- Install FastAPI and Uvicorn
- Create a main application file (e.g., `main.py`)
- Implement a root endpoint (`/`) that returns a welcome message as JSON

### 🛠️ Task 2: Create CRUD Endpoints

#### Description
Add endpoints to perform Create, Read, Update, and Delete (CRUD) operations for a simple resource (e.g., items).

#### Requirements
Completed program should:
- Define a data model for the resource (e.g., Item with id, name, description)
- Implement endpoints for:
  - Creating a new item (`POST /items`)
  - Reading all items (`GET /items`)
  - Reading a single item by id (`GET /items/{id}`)
  - Updating an item (`PUT /items/{id}`)
  - Deleting an item (`DELETE /items/{id}`)
- Return appropriate JSON responses and status codes
