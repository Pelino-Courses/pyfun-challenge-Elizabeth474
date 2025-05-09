from abc import ABC, abstractmethod
from typing import List, Iterator

# Descriptor for attribute validation
class NonEmptyString:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{self.name} must be a non-empty string")
        instance.__dict__[self.name] = value

# Base class
class Person(ABC):
    name = NonEmptyString('name')

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_role(self) -> str:
        pass

# Student and Instructor classes
class Student(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.courses: List[str] = []

    def enroll(self, course_name: str):
        self.courses.append(course_name)

    def __iter__(self) -> Iterator[str]:
        return iter(self.courses)

    def get_role(self) -> str:
        return "Student"

class Instructor(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.courses: List[str] = []

    def assign_course(self, course_name: str):
        self.courses.append(course_name)

    def get_role(self) -> str:
        return "Instructor"

# Multiple inheritance: Teaching Assistant
class TeachingAssistant(Student, Instructor):
    def get_role(self) -> str:
        return "Teaching Assistant"

# Course class
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

    def __str__(self):
        return f"Course: {self.name}, Instructor: {self.instructor.name}, Students: {[student.name for student in self.students]}"

# Enrollment class
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

# Factory methods for courses
class CourseFactory:
    @staticmethod
    def create_course(name: str, instructor: Instructor) -> Course:
        return Course(name, instructor)

# Testing the system
instructor1 = Instructor("Dr. Smith")
course1 = CourseFactory.create_course("Math 101", instructor1)

student1 = Student("Alice")
student2 = Student("Bob")
ta1 = TeachingAssistant("Charlie")

enrollment = Enrollment()
enrollment.enroll_student(student1, course1)
enrollment.enroll_student(student2, course1)
enrollment.enroll_student(ta1, course1)

# Print enrolled students
for enrollment_info in enrollment:
    print(enrollment_info)

# Iterate through a student's courses
student1.enroll(course1.name)
for course_name in student1:
    print(f"Alice is taking: {course_name}")

# Operator overloading test (+)
course2 = CourseFactory.create_course("Physics 101", instructor1)
combined_course = course1 + course2
print(f"Combined Course: {combined_course.name}")
    