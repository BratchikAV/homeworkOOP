class Student:
    name = " "
    surname = " "
    gender = " "

    def __init__(self):
        self.finished_courses = []
        self.marks = []
        self.grades = {}


class Mentor:
    name = " "
    surname = " "

    def __init__(self):
        self.courses_attached = []
