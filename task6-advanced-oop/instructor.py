from person import Person

class Instructor(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.courses = []

    def assign_course(self, course_name: str):
        self.courses.append(course_name)

    def get_role(self) -> str:
        return "Instructor"
