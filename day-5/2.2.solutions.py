class School:
    # classes = []
    pass


class Class:
    # students = []
    pass


class Student:
    # name = ""
    # score = ""
    pass


school = School()

class_a = Class()
class_b = Class()

student_1 = Student()
student_1.name = "mahdi"
student_1.score = 20

student_2 = Student()
student_2.name = "ali"
student_2.score = 18

student_3 = Student()
student_3.name = "reza"
student_3.score = 15

school.classes = []
school.classes.append(class_a)
school.classes.append(class_b)

class_a.students = []
class_b.students = []

class_a.students.append(student_1)
class_a.students.append(student_2)

class_b.students.append(student_3)

# solution 1
for my_class in school.classes:
    print("- class:")

    print(my_class.students)

    student_scores = []

    for student in my_class.students:
        student_scores.append(student.score)

    my_min = min(student_scores)
    my_max = max(student_scores)
    my_sum = sum(student_scores)
    my_len = len(student_scores)
    my_avg = my_sum / my_len

    print("student count", my_len)
    print("min score", my_min)
    print("max score", my_max)
    print("avg score", my_avg)
    print("sum score", my_sum)


# solution 2
for my_class in school.classes:
    print("- class:")

    print(my_class.students)

    student_scores = [student.score for student in my_class.students]

    my_min = min(my_class.students, key=lambda element: element.score).score
    my_max = max(my_class.students, key=lambda element: element.score).score
    my_sum = sum([student.score for student in my_class.students])
    my_len = len(my_class.students)
    my_avg = my_sum / my_len

    print("student count", my_len)
    print("min score", my_min)
    print("max score", my_max)
    print("avg score", my_avg)
    print("sum score", my_sum)
