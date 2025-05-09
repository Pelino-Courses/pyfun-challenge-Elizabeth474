from person import Person
from typing import List, Iterator

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

