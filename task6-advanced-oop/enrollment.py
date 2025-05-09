from student import Student
from course import Course
from typing import Iterator

class Enrollment:
    def __init__(self):
        self.enrollments = {}

    def enroll_student(self, student: Student, course: Course):
        if course not in self.enrollments:
            self.enrollments[course] = []
        if student in self.enrollments[course]:
            raise ValueError(f"{student.name} is already enrolled in {course.name}.")
        self.enrollments[course].append(student)
        student.enroll(course.name)

    def __iter__(self) -> Iterator[str]:
        for course, students in self.enrollments.items():
            for student in students:
                yield f"{student.name} is enrolled in {course.name}"
