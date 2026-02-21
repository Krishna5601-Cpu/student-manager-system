# Student Management System (Python CLI)

A simple but structured **Student Management System** built using Python and a command-line interface.

This project started as a basic CRUD practice project, but gradually evolved into a more **realistic backend-style application** while learning Python fundamentals, clean code practices, and object-oriented design.

The main goal of this project was not just to make something work, but to understand **how real applications are structured internally**.

---

## 🚀 Features

- Add new students
- View all students
- Update student details
- Delete students with confirmation
- Input validation handled inside the model
- Persistent storage using JSON
- Multiple command aliases for better CLI usability
- Modular project structure

---

## 🧠 Learning Focus Behind This Project

Instead of keeping everything inside one file, this project was intentionally refactored step-by-step to learn:

- Separation of concerns
- Object-Oriented Programming (OOP)
- Clean architecture basics
- Data validation at the model level
- Safe refactoring without breaking functionality
- Realistic backend project organization

The system now uses a **Student model** instead of raw dictionaries, along with a mapper layer to convert data between Python objects and JSON storage.

---

## 📁 Project Structure

student-manager-system/
│
├── main.py # Application entry point (menu & command routing)
├── services.py # Business logic (CRUD operations)
├── models.py # Student class (domain model + validation)
├── mappers.py # Dict ↔ Object conversion layer
├── storage.py # JSON load/save handling
├── utils.py # Helper functions
├── students.json # Persistent data storage
└── README.md

---

## ⚙️ Technologies Used

- Python 3.x
- Standard Library only (`json`, `os`)
- Command Line Interface (CLI)

No external libraries were used intentionally to focus on core Python concepts.

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/Krishna5601-Cpu/student-manager-system.git

Go into the project folder:

cd student-manager-system

Run the program:

python main.py
💻 Example Commands

You can use either numbers or text commands:

Action	Commands
Add Student	1, add, add student
View Students	2, view
Update Student	3, update
Delete Student	4, delete
Exit	5, exit, quit
✅ Validation Rules

Name must contain at least 2 characters

Age must be between 18 and 25

Invalid data is rejected before saving

Validation is handled inside the Student class to ensure data integrity.

🔒 Data Storage

Student data is stored locally in a JSON file.

The application converts:

JSON data ⇄ Student objects

using a mapper layer, similar to how backend frameworks handle database models internally.

🌱 Future Improvements

Planned upgrades while continuing the learning journey:

Database integration (SQLite/PostgreSQL)

REST API version using FastAPI

Authentication system

Automated tests (pytest)

Docker & deployment

CI/CD pipeline
```
