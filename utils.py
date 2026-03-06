def get_student_by_id(data, student_id):
    for student in data.get("students", []):
        if student["id"] == student_id:
            return student
    return None

import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause_and_clear():
    input("\nPress Enter to continue...")
    clear_terminal()