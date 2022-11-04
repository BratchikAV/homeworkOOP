class Students:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}
        self.all_marks = []
        # self.rating = round(sum(sum(list(self.grades.values()), [])) / len(sum(list(self.grades.values()), [])), 1)

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {round(sum(self.all_marks) / len(self.all_marks), 1)}
Курсы в процессе изучения: {self.courses_in_progress} 
Завершенные курсы: {self.finished_courses}"""

    def rate_lection(self, lector, course, mark):
        if isinstance(lector, Lecturers) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.all_marks.append(mark)
                lector.grades[course] += [mark]
            else:
                lector.all_marks.append(mark)
                lector.grades[course] = [mark]
        else:
            return 'Error'

    def comparison(self, student):
        if isinstance(student, Students):
            if round(sum(self.all_marks) / len(self.all_marks), 1) > round(sum(student.all_marks) / len(student.all_marks), 1):
                return f"{self.name} {self.surname} ({round(sum(self.all_marks) / len(self.all_marks), 1)}) > {student.name} {student.surname} ({round(sum(student.all_marks) / len(student.all_marks), 1)})"
            elif round(sum(self.all_marks) / len(self.all_marks), 1) < round(sum(student.all_marks) / len(student.all_marks), 1):
                return f"{self.name} {self.surname} ({round(sum(self.all_marks) / len(self.all_marks), 1)}) < {student.name} {student.surname} ({round(sum(student.all_marks) / len(student.all_marks), 1)})"
            else:
                return f"{self.name} {self.surname} ({round(sum(self.all_marks) / len(self.all_marks), 1)}) = {student.name} {student.surname} ({round(sum(student.all_marks) / len(student.all_marks), 1)})"
        else:
            return "Error"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturers(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.all_marks = []

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {round(sum(self.all_marks) / len(self.all_marks), 1)}"""

    def comparison(self, lector):
        if isinstance(lector, Lecturers):
            if round(sum(self.all_marks) / len(self.all_marks), 1) > round(sum(lector.all_marks) / len(lector.all_marks), 1):
                return f"{self.name} {self.surname} ({round(sum(self.all_marks) / len(self.all_marks), 1)}) > {lector.name} {lector.surname} ({round(sum(lector.all_marks) / len(lector.all_marks), 1)})"
            elif round(sum(self.all_marks) / len(self.all_marks), 1) < round(sum(lector.all_marks) / len(lector.all_marks), 1):
                return f"{self.name} {self.surname} ({round(sum(self.all_marks) / len(self.all_marks), 1)}) < {lector.name} {lector.surname} ({round(sum(lector.all_marks) / len(lector.all_marks), 1)})"
            else:
                return f"{self.name} {self.surname} ({round(sum(self.all_marks) / len(self.all_marks), 1)}) = {lector.name} {lector.surname} ({round(sum(lector.all_marks) / len(lector.all_marks), 1)})"
        else:
            return "Error"


class Reviewers(Mentor):
    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}"""


    def rate_hw(self, student, course, mark):
        if isinstance(student, Students) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.all_marks.append(mark)
                student.grades[course] += [mark]
            else:
                student.all_marks.append(mark)
                student.grades[course] = [mark]
        else:
            return 'Error'



student_1 = Students("Mike", "Tyson", "man")
aspirant = Students("Albert", "Einstein", "man")
student_1.courses_in_progress += ["Python.Списки"]
student_1.courses_in_progress += ["Python.Словари"]
student_1.courses_in_progress += ["GIT"]
student_1.courses_in_progress += ["Python.ООП"]
student_1.finished_courses += ["Visual Basic"]
aspirant.courses_in_progress += ["Python.Списки"]
aspirant.courses_in_progress += ["Python.Словари"]
aspirant.courses_in_progress += ["GIT"]
aspirant.courses_in_progress += ["Python.ООП"]
aspirant.finished_courses += ["Visual Basic"]
reviewer_1 = Reviewers("Adam", "Smith")
reviewer_1.courses_attached += ["Python"]
reviewer_1.courses_attached += ["Python.Списки"]
reviewer_1.courses_attached += ["Python.Словари"]
reviewer_1.courses_attached += ["GIT"]
reviewer_1.courses_attached += ["Python.ООП"]
reviewer_1.rate_hw(student_1, "GIT", 7)
reviewer_1.rate_hw(student_1, "GIT", 8)
reviewer_1.rate_hw(student_1, "Python.ООП", 7)
reviewer_1.rate_hw(aspirant, "GIT", 10)
reviewer_1.rate_hw(aspirant, "GIT", 10)
reviewer_1.rate_hw(aspirant, "Python.ООП", 10)
lector_1 = Lecturers("Billy", "Milligan")
lector_1.courses_attached += ["Python.Списки"]
lector_1.courses_attached += ["Python.Словари"]
lector_1.courses_attached += ["GIT"]
lector_1.courses_attached += ["Python.ООП"]
student_1.rate_lection(lector_1, "Python.ООП", 9)
student_1.rate_lection(lector_1, "Python.Списки", 9)
student_1.rate_lection(lector_1, "Python.ООП", 8)
student_1.rate_lection(lector_1, "Python.Списки", 9)
professor = Lecturers("Нереально", "Умный")
professor.courses_attached += ["Python.Списки"]
professor.courses_attached += ["Python.Словари"]
professor.courses_attached += ["GIT"]
professor.courses_attached += ["Python.ООП"]
student_1.rate_lection(professor, "Python.ООП", 10)
student_1.rate_lection(professor, "GIT", 9)
student_1.rate_lection(professor, "Python.ООП", 10)
student_1.rate_lection(professor, "Python.Словари", 10)


print(student_1.comparison(aspirant))
print(lector_1.comparison(professor))
print("-------------------")
print(aspirant.comparison(student_1))
print(professor.comparison(lector_1))


