class Students:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}

    def rate_lection(self, lector, course, mark):
        if isinstance(lector, Lecturers) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [mark]
            else:
                lector.grades[course] = [mark]
        else:
            return 'Error'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturers(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}



class Reviewers(Mentor):
    def rate_hw(self, student, course, mark):
        if isinstance(student, Students) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [mark]
            else:
                student.grades[course] = [mark]
        else:
            return 'Error'



student_1 = Students("Mike", "Tyson", "man")
student_1.courses_in_progress += ["Python"]
reviewer_1 = Reviewers("Adam", "Smith")
reviewer_1.courses_attached += ["Python"]
reviewer_1.rate_hw(student_1, "Python", 7)
reviewer_1.rate_hw(student_1, "Python", 8)
reviewer_1.rate_hw(student_1, "Python", 7)
lector_1 = Lecturers("Billy", "Milligan")
lector_1.courses_attached += ["Python"]
student_1.rate_lection(lector_1, "Python", 9)
student_1.rate_lection(lector_1, "Python", 9)
student_1.rate_lection(lector_1, "Python", 8)
student_1.rate_lection(lector_1, "Python", 9)

print(student_1.name)
print(student_1.surname)
print(student_1.grades)
print(lector_1.grades)
