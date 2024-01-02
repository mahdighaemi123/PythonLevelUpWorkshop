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
class_count = int(input("enter class count: "))

school.classes = []
for i in range(class_count):
    c = Class()
    school.classes.append(c)

    student_count = int(input("enter student count: "))
    
    c.students = []
    for j in range(student_count):
        data = input("enter student name and score: ")
        name,score = data.split()

        s = Student()
        s.name = name
        s.score = score
        c.students.append(s)

print("school:")
print()

# solution 1
for i in range(len(school.classes)):
    print(f"- class {i+1}:")
    student_count = len(school.classes[i].students)
    for j in range(student_count):
        student = school.classes[i].students[j]
        print(f"  {student.name} {student.score}")
    print()

# solution 2
for c in school.classes:
    print("- class: ")

    for s in c.students:
        print(f"  {s.name} {s.score}")

    print()
