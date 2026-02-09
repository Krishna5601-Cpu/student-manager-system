from storage import load_data, save_data
from validators import validate_age, validate_name
from utils import get_student_by_id


def view_students(data):
    """
    Display all students in a readable CLI format.
    """
    students = data.get("students", [])

    if not students:
        print("No students found.")
        return

    for student in students:
        print(f"ID: {student.get('id')}")
        print(f"Name: {student.get('name')}")
        print(f"Age: {student.get('age')}")
        print(f"Course: {student.get('course')}")
        print("-" * 20)


def add_student(data):
    """
    Add a new student and persist data to JSON.
    """
    students = data.get("students", [])

    name = input("Enter student name: ")
    if not validate_name(name):
        print("Invalid name.")
        return

    try:
        age = int(input("Enter student age: "))
    except ValueError:
        print("Age must be a number.")
        return

    if not validate_age(age):
        print("Invalid age. Age must be between 18 and 25.")
        return

    course = input("Enter student course: ")

    # Generate unique ID
    if students:
        new_id = max(student["id"] for student in students) + 1
    else:
        new_id = 1

    new_student = {
        "id": new_id,
        "name": name,
        "age": age,
        "course": course,
    }

    students.append(new_student)
    save_data(data)

    print("Student added successfully.")


def update_student(data):
    students = data.get("students", [])

    if not students:
        print("No students available to update.")
        return

    try:
        student_id = int(input("Enter the student ID to update: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    student = get_student_by_id(data, student_id)

    if not student:
        print("Student ID not found.")
        return

    print("\nCurrent student details:")
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Course: {student['course']}")
    print("-" * 20)

    new_name = input("Enter new name (press Enter to skip): ").strip()
    if new_name:
        if not validate_name(new_name):
            print("Invalid name.")
            return
        student["name"] = new_name

    new_age = input("Enter new age (press Enter to skip): ").strip()
    if new_age:
        try:
            age = int(new_age)
        except ValueError:
            print("Age must be a number.")
            return

        if not validate_age(age):
            print("Invalid age. Age must be between 18 and 25.")
            return

        student["age"] = age

    new_course = input("Enter new course (press Enter to skip): ").strip()
    if new_course:
        student["course"] = new_course

    save_data(data)
    print("Student updated successfully.")


def delete_student(data):
    students = data.get("students", [])

    if not students:
        print("No students available to delete.")
        return

    try:
        student_id = int(input("Enter the student ID to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    student = get_student_by_id(data, student_id)

    if not student:
        print("Student ID not found.")
        return

    print("\nStudent found:")
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Course: {student['course']}")
    print("-" * 20)

    confirm = (
        input("Are you sure you want to delete this student? (yes/no): ")
        .strip()
        .lower()
    )

    if confirm in {"y", "yes"}:
        index = students.index(student)
        students.pop(index)
        save_data(data)
        print("Student deleted successfully.")
    else:
        print("Deletion cancelled.")
