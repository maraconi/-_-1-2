class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.lecture_courses and course in self.courses_in_progress:
            if course in lecture.lecture_grades:
                lecture.lecture_grades[course] += grade
            else:
                lecture.lecture_grades[course] = grade
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = ['Python', 'Git']


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_courses = []
        self.lecture_grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка'


student_1 = Student('Ivan', 'Petrov', 'your_gender')
student_1.courses_in_progress += ['Python', 'Git']
student_2 = Student('Lev', 'Sidorov', 'your_gender')
student_2.courses_in_progress += ['Python', 'Git']

lecture_1 = Lecturer('Pavel', 'Loginov')
lecture_1.lecture_courses = ['Python']
student_1.rate_lector(lecture_1, 'Python', [7])
student_2.rate_lector(lecture_1, 'Python', [9])
lecture_2 = Lecturer('Alex', 'Barinov')
lecture_2.lecture_courses = ['Git']
student_2.rate_lector(lecture_2, 'Git', [8])
student_1.rate_lector(lecture_2, 'Git', [10])

reviewer_1 = Reviewer('Matvey', 'Kazak')
reviewer_1.rate_hw(student_1, 'Python', [7, 8, 10, 9])
reviewer_1.rate_hw(student_2, 'Python', [10, 8, 10, 10])
reviewer_2 = Reviewer('Irina', 'Kazak')
reviewer_2.rate_hw(student_1, 'Git', [9, 8, 9, 9])
reviewer_2.rate_hw(student_2, 'Git', [10, 8, 10, 9])

# Проверка вывода кода
print(student_1.name, student_1.surname, ',', student_1.gender)
print(student_1.courses_in_progress)
print(student_1.grades)
print(student_2.name, student_2.surname, ',', student_2.gender)
print(student_2.courses_in_progress)
print(student_2.grades, '\n')

print(reviewer_1.name, reviewer_1.surname)
print(reviewer_1.courses_attached)
print(reviewer_2.name, reviewer_2.surname)
print(reviewer_2.courses_attached, '\n')

print(lecture_1.name, lecture_1.surname)
print(lecture_1.lecture_courses)
print(lecture_1.lecture_grades)
print(lecture_2.name, lecture_2.surname)
print(lecture_2.lecture_courses)
print(lecture_2.lecture_grades)