from typing import List, Iterator
from instructor import Instructor
from student import Student

class Course:
    def __init__(self, name: str, instructor: Instructor):
        self.name = name
        self.instructor = instructor
        self.students: List[Student] = []

    def add_student(self, student: Student):
        self.students.append(student)

    def __iter__(self) -> Iterator[str]:
        return iter([student.name for student in self.students])

    def __add__(self, other):
        if isinstance(other, Course):
            combined_course = Course(f"{self.name} & {other.name}", self.instructor)
            combined_course.students = self.students + other.students
            return combined_course
        raise TypeError("Can only add Course objects")
