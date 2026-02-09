# student-manager-system

# Student Management System (Python CLI)

A modular, production-style **Student Management System** built using Python.  
This project demonstrates clean architecture, CRUD operations, input validation,
and real-world backend design principles using a command-line interface (CLI).

---

## 🚀 Features

- Add new students
- View all students
- Update existing student details
- Delete students safely with confirmation
- Input validation (name, age, ID)
- Persistent storage using JSON
- Modular and scalable project structure
- Command aliases for better UX

---

## 🧠 What This Project Demonstrates

This project is intentionally designed to reflect **real backend development practices**:

- Separation of concerns
- Defensive programming
- Clean, readable code
- Reusable helper utilities
- Business rule validation
- Refactoring without breaking behavior

---

## 🗂 Project Structure

```text
student_manager/
│
├── main.py          # Application entry point (menu & routing)
├── storage.py       # JSON file handling (load/save)
├── services.py      # Core business logic (CRUD operations)
├── validators.py    # Input validation rules
├── utils.py         # Helper utilities (ID lookup)
├── students.json    # Persistent data storage
└── README.md


 🛠 Technologies Used

Python 3.x

Core Python Libraries  only (json, os)

CLI-based interaction



▶️ How to Run the Project

1 - Clone the repository:

git clone https://github.com/your-username/student-management-system.git


2 - Navigate to the project directory:

cd student-management-system


3 - Run the application:

python main.py



🧪 Example Commands

You can interact using numbers or aliases:

1 or add → Add student

2 or view → View students

3 or update → Update student

4 or delete → Delete student

5 or exit → Exit program


📌 Validation Rules
<ul>
<li> Name: Minimum 2 characters, cannot be empty </li>

<li> Age: Must be between 18 and 25 </li>

<li> ID: Must be unique and exist for update/delete operations </li>
</ul>


🔒 Data Safety

* All destructive actions require confirmation

* Invalid input is safely handled

* Data integrity is preserved across operations


🌱 Future Improvements

Migrate from JSON to a database (SQLite/PostgreSQL)

- Add authentication

- Convert CLI to REST API using FastAPI

- Add automated tests

- Add CI/CD pipeline using GitHub Actions

```
