from models import Student


def student_from_dict(data: dict) -> Student:
    return Student(
        data["id"],
        data["name"],
        data["age"],
        data["course"],
    )


def student_to_dict(student: Student) -> dict:
    return {
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "course": student.course,
    }
