# To-Do App

A simple and user-friendly task management app built with Django and Bootstrap. Users can create, update, delete, and filter their tasks efficiently with a clean and responsive interface.


## Features

- User Authentication (Register, Login, Logout)
- Add New Task
- Update Existing Task
- Delete Task
- Upload Task List (from Excel)
- Download Task List (as Excel)
- Filter Tasks by Completion Date and Status
- Mark Tasks as Completed
- Fully Responsive with Bootstrap 5


## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Bootstrap 5 + HTML Templates
- **Database:** SQLite (default)
- **Other:** Django Messages Framework, Static Files,Selenium,Excel Support via `pandas` or `openpyxl`


##  Installation Guide for To do App Project

### 1. Clone the repository
git clone https://github.com/Darpan-Anjanay/TodoList.git  # Download the project from GitHub
cd todolist  # Move into the project directory

### 2. Create a virtual environment
python -m venv venv  # Create a virtual environment named 'venv'

### 3. Activate the virtual environment

venv\Scripts\activate  # For Windows

### 4.Install the project dependencies
pip install -r requirements.txt  # Install all required packages listed in requirements.txt

### 5. Set up the database
python manage.py makemigrations  # Generate migration files based on the models
python manage.py migrate  # Apply the migrations to create the database schema

### 6. Create a superuser for accessing the Django admin panel
python manage.py createsuperuser  # Follow the prompts (username, email, password)

### 7. Run the development server
python manage.py runserver  # Start the local server

#  Now, open your browser and go to: http://127.0.0.1:8000/
#  To access the admin panel, visit: http://127.0.0.1:8000/admin/
 


## Testing
Running Unit and Integration Tests
The project uses Django’s built-in testing framework.

To run all tests, activate your virtual environment and run : python manage.py test


## Selenium End-to-End Testing
End-to-end tests are implemented using Selenium WebDriver to automate browser interaction and test the full app flow.

## Setup
Ensure Google Chrome is installed.
Install Selenium and WebDriver Manager : pip install selenium webdriver-manager
Running Selenium Tests:python manage.py test TodoApp.tests_selenium

## Author

- **Name:** Darpan Anjanay
- **GitHub:** https://github.com/Darpan-Anjanay/


# Screenshots

## Register Page
![Register Page](/screenshots/register.png)

## Login Page
![Login Page](/screenshots/login.png)

## Home Page
![Home Page](/screenshots/home.png)

## Add Task Page
![Add Task Page](/screenshots/add.png)

## Upload Task Page
![Upload Task Page](/screenshots/upload.png)

