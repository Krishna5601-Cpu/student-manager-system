import json
import os
from storage import load_data
from services import (
    add_student,
    view_students,
    update_student,
    delete_student,
)


FILE_NAME = "students.json"


def main():
    data = load_data()

    commands = {
        "1": add_student,
        "add": add_student,
        "add student": add_student,
        "2": view_students,
        "view": view_students,
        "view students": view_students,
        "3": update_student,
        "update": update_student,
        "update student": update_student,
        "4": delete_student,
        "delete": delete_student,
        "delete student": delete_student,
        "5": "exit",
        "exit": "exit",
        "quit": "exit",
    }

    while True:
        print("\n" + "=" * 40)
        print("Student Management System")
        print("=" * 40)
        print("1. Add student")
        print("2. View students")
        print("3. Update student")
        print("4. Delete student")
        print("5. Exit")
        print("=" * 40)

        choice = input("Enter your choice: ").strip().lower()

        action = commands.get(choice)

        if action == "exit":
            print("Exiting program. Goodbye!")
            break

        elif callable(action):
            action(data)

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
