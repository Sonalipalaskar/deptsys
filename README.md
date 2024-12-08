
# Department Management System

## Overview
This is a simple Django-based application for managing departments within an organization. The system allows users to create, update, delete, and search for departments. It provides a user-friendly interface to perform CRUD operations (Create, Read, Update, Delete) on department data.

## Features
- **Create Department**: Users can add a new department by providing the department's name and description.
- **Update Department**: Users can update the details of an existing department.
- **Delete Department**: Departments can be marked as inactive (soft delete) by changing their status to False.
- **Search Departments**: Users can search for departments by name using a search bar.
- **View Department List**: The application displays all active departments in a table format.

## Technologies Used
- **Django**: Python web framework for building the backend.
- **HTML/CSS**: For the frontend user interface.
- **Bootstrap**: For responsive and styled components.
- **SQLite**: For the database (default Django database).

## Setup Instructions

### Prerequisites
1. Python (>=3.8)
2. Django (>=4.0)

### Installation Steps

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/department-management-system.git
    cd department-management-system
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the migrations to set up the database:**
    ```bash
    python manage.py migrate
    ```

4. **Create a superuser to access the admin interface:**
    ```bash
    python manage.py createsuperuser
    ```

5. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Access the application** by navigating to `http://127.0.0.1:8000/` in your browser.

## Endpoints
- **Home** (`/`): Displays the list of departments.
- **Create Department** (`/create`): Form to create a new department.
- **Update Department** (`/update/<dept_id>`): Form to update department details.
- **Delete Department** (`/delete/<dept_id>`): Mark a department as inactive.
- **Search** (`/searchtext/`): Search for departments by name.

## Directory Structure

```
project/
│
├── deptapp/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       ├── base.html
│       ├── createdept.html
│       ├── index.html
│       ├── updatedept.html
│
├── manage.py
├── requirements.txt
└── db.sqlite3
```

## Author
Sonali Palaskar (sonalipalaskar598@gmail.com)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
