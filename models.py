class Student:
    def __init__(self, student_id, name, age, course):
        if not name or len(name.strip()) < 2:
            raise ValueError("Invalid name")

        if age < 18 or age > 25:
            raise ValueError("Invalid age")

        self.id = student_id
        self.name = name
        self.age = age
        self.course = course

    def update_name(self, new_name):
        if not new_name or len(new_name.strip()) < 2:
            raise ValueError("Invalid name")
        self.name = new_name

    def update_age(self, new_age):
        if new_age < 18 or new_age > 25:
            raise ValueError("Invalid age")
        self.age = new_age

    def update_course(self, new_course):
        if not new_course or not new_course.strip():
            raise ValueError("Invalid course")
        self.course = new_course
