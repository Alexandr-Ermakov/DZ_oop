list_of_students = []
list_of_lecturers = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.sum_of_grades = 0
        self.number_of_grades = 0
        list_of_students.append(self)

    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)

    def add_courses_in_progress(self, course_name):
        self.courses_in_progress.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                lecturer.sum_of_grades += grade
                lecturer.number_of_grades += 1
            else:
                lecturer.grades[course] = [grade]
                lecturer.sum_of_grades += grade
                lecturer.number_of_grades += 1
        else:
            print('Error')

    def __str__(self):
        self.list_of_courses_progress = ''
        self.list_of_finished_courses = ''

        for element in self.courses_in_progress:
            self.list_of_courses_progress += element
            if element != self.courses_in_progress[-1]:
                self.list_of_courses_progress += ', '

        for element in self.finished_courses:
            self.list_of_finished_courses += element
            if element != self.finished_courses[-1]:
                self.list_of_finished_courses += ', '

        result = (f'Имя: {self.name}\n'
                  f'Фамилия: {self.surname}\n'
                  f'Средняя оценка за домашние задания: {self.sum_of_grades / self.number_of_grades}\n'
                  f'Курсы в процессе изучения: {self.list_of_courses_progress}\n'
                  f'Завершенные курсы: {self.list_of_finished_courses}\n')
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'He (she) is not a Student!'
        else:
            return self.sum_of_grades / self.number_of_grades < other.sum_of_grades / other.number_of_grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_courses_attached(self, course_name):
        self.courses_attached.append(course_name)

    def __str__(self):
        result = (f'Имя: {self.name}\n'
                  f'Фамилия: {self.surname}\n')
        return result


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.sum_of_grades = 0
        self.number_of_grades = 0
        list_of_lecturers.append(self)

    def __str__(self):
        return super(Lecturer,
                     self).__str__() + f'Средняя оценка за лекции: {self.sum_of_grades / self.number_of_grades}\n'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'He (she) is not a Lecturer!'
        else:
            return self.sum_of_grades / self.number_of_grades < other.sum_of_grades / other.number_of_grades


class Reviewer(Mentor):

    def rate_student_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                student.sum_of_grades += grade
                student.number_of_grades += 1
            else:
                student.grades[course] = [grade]
                student.sum_of_grades += grade
                student.number_of_grades += 1
        else:
            print('Error')


def count_middle_grade_of_students(list, course_name):
    sum_of_grades = 0
    number_of_grades = 0
    for student in list:
        for course, grades in student.grades.items():
            if course == course_name:
                for mark in grades:
                    sum_of_grades += mark
                    number_of_grades += 1
    if number_of_grades != 0:
        print(f'Average grade = {sum_of_grades / number_of_grades}')
        return
    else:
        print('Not enough data')


def count_middle_grade_of_lecturers(list, course_name):
    sum_of_grades = 0
    number_of_grades = 0
    for lecturer in list:
        for course, grades in lecturer.grades.items():
            if course == course_name:
                for mark in grades:
                    sum_of_grades += mark
                    number_of_grades += 1
    if number_of_grades != 0:
        print(f'Average grade = {sum_of_grades / number_of_grades}')
        return
    else:
        print('Not enough data')


student_one = Student('Viktor', 'Viktorov', 'male')
student_two = Student('Boris', 'Svistunov', 'female')

mentor_one = Mentor('Eldar', 'Faruhov')
mentor_two = Mentor('Marina', 'Kashina')

lecturer_one = Lecturer('Pavel', 'Karpov')
lecturer_two = Lecturer('Katrina', 'Messing')

reviewer_one = Reviewer('Slava', 'Arnoldov')
reviewer_two = Reviewer('Zinaida', 'Aramova')

student_one.add_finished_courses('Python beginner')
student_one.add_finished_courses('Java Script beginner')
student_one.add_courses_in_progress('Python')
student_one.add_courses_in_progress('Java Script')

student_two.add_courses_in_progress('Java Script')
student_two.add_courses_in_progress('Python')

mentor_one.add_courses_attached('Python')
mentor_one.add_courses_attached('Java Script')

mentor_two.add_courses_attached('Python')
mentor_two.add_courses_attached('Java Script')

lecturer_one.add_courses_attached('Python')
lecturer_one.add_courses_attached('Java Script')

lecturer_two.add_courses_attached('Java Script')
lecturer_two.add_courses_attached('Python')

student_one.rate_lecturer(lecturer_one, 'Python', 10)
student_one.rate_lecturer(lecturer_two, 'Python', 5)
student_one.rate_lecturer(lecturer_one, 'Java Script', 6)
student_one.rate_lecturer(lecturer_two, 'Java Script', 4)

student_two.rate_lecturer(lecturer_one, 'Python', 9)
student_two.rate_lecturer(lecturer_two, 'Python', 4)
student_two.rate_lecturer(lecturer_one, 'Java Script', 5)
student_two.rate_lecturer(lecturer_two, 'Java Script', 2)

reviewer_one.add_courses_attached('Python')
reviewer_one.add_courses_attached('Java Script')
reviewer_one.rate_student_hw(student_one, 'Python', 10)
reviewer_one.rate_student_hw(student_one, 'Java Script', 9)
reviewer_one.rate_student_hw(student_two, 'Python', 10)
reviewer_one.rate_student_hw(student_two, 'Java Script', 10)

reviewer_two.add_courses_attached('Python')
reviewer_two.add_courses_attached('Java Script')
reviewer_two.rate_student_hw(student_one, 'Python', 5)
reviewer_two.rate_student_hw(student_one, 'Java Script', 3)
reviewer_two.rate_student_hw(student_two, 'Python', 10)
reviewer_two.rate_student_hw(student_two, 'Java Script', 6)

print(student_one.__dict__)
print(student_two.__dict__)
print(mentor_one.__dict__)
print(mentor_two.__dict__)
print(lecturer_one.__dict__)
print(lecturer_two.__dict__)
print(reviewer_one.__dict__)
print(reviewer_two.__dict__)
print()
print(student_one)
print(student_two)
print(mentor_one)
print(mentor_two)
print(lecturer_one)
print(lecturer_two)
print(reviewer_one)
print(reviewer_two)
print()
print(student_one < student_two)
print(lecturer_one < lecturer_two)
print()
count_middle_grade_of_students(list_of_students, 'Python')
count_middle_grade_of_lecturers(list_of_lecturers, 'Java Script')