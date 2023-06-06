class Enroll: 
    # courses = []

    def __init__(self , student_name):
        self.name = student_name
        self.courses = []
    def add_course(self , couse_name):
        self.courses.append(couse_name)
    # def display(self):
    #     print(f'Student Name :{self.name} , Course Name :{self.course}')

ahmad = Enroll('Ahmad H')
khalid = Enroll('Khalid H')

ahmad.add_course('ML')
ahmad.add_course('NLP')

khalid.add_course('AI')
khalid.add_course('Web')

print(ahmad.courses)
print(khalid.courses)