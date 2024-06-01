class Student:
    
    school = "Akirachix"
    

    def __init__(self,first_name,last_name,age,country,code,school):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.code = code
        self.school=school
    def greet_student(self):
            print(f"Hello {self.first_name} welcome to {self.school} your code is {self.code}")
    def year_born(self):
        print(f"hello {self.first_name} you were born in {2024 -self.age} ") 
    def full_name(self):
        print(f"hello {self.first_name} {self.last_name}")
    def enroll_student(self):
        print(f"{self.first_name} congratulations you have successfully been enrolled to {self.school}")  
    def student_initials(self):
        print(f"ramla ali your initials are {self.first_name[0]} and {self.last_name[0]}")



# mercy = Student(first_name="mercy",last_name="chemtai",age=20,country="kenya",code=44)
# aline = Student(first_name="aline",last_name="mutesi",age=24,country="Rwanda",code=34)
# eshe = Student(first_name="eshe",last_name="aziz",age=30,country="kenya",code=40)

    