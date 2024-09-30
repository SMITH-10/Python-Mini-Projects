# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return  self.age
#     def set_age(self,age):
#         self.age=age

# # d=Dog("Tim",34)
# # print(d.get_name())
# # d2=Dog("Bill",21)
# # print(d2.get_name())

# dogs_name=["Tim","Bill"]
# dogs_age=[23,12]

# # dog1_name="Tim"
# # dog1_age=21


class Student:
    def  __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

    def get_grade(self):
        return self.grade


class Course:
    def  __init__(self,name,max_students):
        self.name=name
        self.max_students=max_students
        self.students=[]

    def add_student(self,student):
        if len(self.students)<self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self,):
        value=0
        for student in self.students:
            value+=student.get_grade()

        return value/len(self.students)

s1=Student("Tim",19,95)
s2=Student("Bill",19,75)
s3=Student("Smith",19,98)

course=Course("Science",3)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.students[0].name)
print(course.get_average_grade())