# import mean() function to calculate arithmetic mean
from cgi import print_directory
from statistics import mean

class Student:
    students = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grade_list = [] 
        Student.students.append(self)


    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
                lecturer.rated.append(rate)
            else:
                lecturer.rates[course] = [rate]
                lecturer.rated.append(rate)
        else:
            return 'Error'

    def __str__(self):
        res = f"Name: {self.name.capitalize()}\n\
Surname: {self.surname}\n\
Arithmetic mean for homeworks: {mean(self.grade_list)}\n\
Courses in process: {', '.join(self.courses_in_progress)}\n\
Finished courses: {', '.join(self.finished_courses)}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a student")
            return 
        return mean(self.grade_list) < mean(other.grade_list)

    def rate_all_stud(students, course):
        all_grades = []
        for student in students:
            if course in student.courses_in_progress or student.finished_courses:
                for grade in student.grades.values():
                        for g in grade:
                            all_grades.append(g)                            
        print(mean(all_grades))

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    lecturers = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rates = {}
        self.rated = []
        Lecturer.lecturers.append(self)

    def __str__(self):
        res = f"Name: {self.name.capitalize()}\n\
Surname: {self.surname}\n\
Arithmetic mean for lectures: {mean(self.rated)}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Not a lecturer")
            return 
        return mean(self.rated) < mean(other.rated)

    def rate_all_lect(lecturers, course):
        all_rates = []
        for lecturer in lecturers:
            if course in lecturer.courses_attached:
                for rate in lecturer.rates.values():
                        for r in rate:
                            all_rates.append(r)                            
        print(mean(all_rates))
    

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                student.grade_list.append(grade)
            else:
                student.grades[course] = [grade]
                student.grade_list.append(grade)
        else:
            return 'Ошибка'
            
    def __str__(self):
        res = f"Name: {self.name.capitalize()}\nSurname: {self.surname}"
        return res


# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
# best_student2 = Student('Ru', 'Em', 'your')
# best_student2.courses_in_progress += ['Python']
# cool_mentor = Reviewer('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 6)
# cool_mentor.rate_hw(best_student2, 'Python', 9)

# Student.rate_all_stud(Student.students, 'Python')

# cool_lecturer = Lecturer('Some', 'Buddy')
# cool_lecturer.courses_attached += ['Python']
# cool_lecturer2 = Lecturer('Some', 'Buddy')
# cool_lecturer2.courses_attached += ['Python']
# best_student.rate_lecturer(cool_lecturer, 'Python', 10)
# best_student.rate_lecturer(cool_lecturer2, 'Python', 5)
# best_student.rate_lecturer(cool_lecturer, 'Python', 9)

# Lecturer.rate_all_lect(Lecturer.lecturers, 'Python')

# print(cool_lecturer < cool_lecturer2)
# print(best_student < best_student2)
# print(best_student)
# print(cool_lecturer)
# print(cool_mentor)