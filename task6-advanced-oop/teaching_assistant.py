from student import Student
from instructor import Instructor

class TeachingAssistant(Student, Instructor):
    def __init__(self, name: str):
        Student.__init__(self, name)
        Instructor.__init__(self, name)

    def get_role(self) -> str:
        return "Teaching Assistant"

