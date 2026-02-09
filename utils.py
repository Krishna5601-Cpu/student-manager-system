def get_student_by_id(data, student_id):
    for student in data.get("students", []):
        if student["id"] == student_id:
            return student
    return None
