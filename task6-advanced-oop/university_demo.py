from instructor import Instructor
from student import Student
from course import Course
from enrollment import Enrollment
from teaching_assistant import TeachingAssistant

# Create Instructor
instructor1 = Instructor("Lecturer. Mugisha")
course1 = Course("Engineering drawing 150", instructor1)

# Create Students
student1 = Student("Lea")
student2 = Student("Ange")
ta1 = TeachingAssistant("Patrick")

# Enroll Students
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
    print(f"Lea is taking: {course_name}")

# Operator overloading test (+)
course2 = Course("Web design 101", instructor1)
combined_course = course1 + course2
print(f"Combined Course: {combined_course.name}")
