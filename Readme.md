# Employee Management System

This is a Django-based web application for managing employees. It allows you to add, update, delete, and view employee details.

## Project Structure

The project is organized into two main Django apps:

1. `employee_management`: This is the main Django app that contains the settings for the project.
2. `employees`: This app handles all the functionalities related to employees.

The `employees` app contains the following important files:

- `models.py`: Defines the `Employee` model that represents an employee in the database.
- `forms.py`: Contains the `EmployeeForm` form for adding and updating employees.
- `views.py`: Contains the views for displaying, adding, and updating employees.
- `urls.py`: Defines the URLs for the `employees` app.

The `employee_management` app contains the following important files:

- `settings.py`: Contains the settings for the Django project.
- `urls.py`: Defines the main URLs for the project.

The `manage.py` script is used to run administrative tasks.

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Activate the virtual environment by running `source venv/Scripts/activate` (on Windows) or `source venv/bin/activate` (on Unix or MacOS).
4. Install the required packages by running `pip install -r requirements.txt`.
5. Run the server by running `python manage.py runserver`.

## Usage

Visit `http://localhost:8000` in your web browser to use the application.

## Contributing

Contributions are welcome. Please open a pull request with your changes.

## License

This project is licensed under the MIT License.
